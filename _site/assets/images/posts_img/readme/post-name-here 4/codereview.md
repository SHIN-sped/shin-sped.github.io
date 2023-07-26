```javascript
window.onload = function() {
  canvas = document.getElementById('canvas');
  ctx = canvas.getContext('2d');
  const margin = 30;
  const cw = (ch = canvas.width = canvas.height = 600 + margin * 2);
  const row = 18; // 오목판 선 개수
  const rowSize = 600 / row; // 오목판 한 칸의 너비
  const dolSize = 13; // 바둑돌 크기
  let count = 0; // 현재까지 놓인 돌의 수를 카운트하는 변수
  let msg = document.querySelector('.message');
  let btn1 = document.querySelector('#reload');
  let btn2 = document.querySelector('#withdraw');
  let board = new Array(Math.pow(row + 1, 2)).fill(-1); // 144개의 배열을 생성하여 -1로 초기화
  let history = new Array(); // 이전 오목판 모양들을 저장하는 배열
  let checkDirection = [
    [1, -1], [1, 0], [1, 1], [0, 1], // 8방향(수직, 수평, 대각선)으로 돌을 확인하기 위한 방향 배열
    [-1, 1], [-1, 0], [-1, -1], [0, -1],
  ];
  const blackWinScreen = document.querySelector('.winShow1'); // 흑돌이 승리했을 때 표시할 화면 요소
  const whiteWinScreen = document.querySelector('.winShow2'); // 백돌이 승리했을 때 표시할 화면 요소
  let audio1 = new Audio('tik.mp3'); // 바둑돌을 놓을 때 재생할 소리 파일
  let audio2 = new Audio('beep.wav'); // 이미 놓여진 자리에 돌을 놓을 때 재생할 경고 소리 파일
  let audio3 = new Audio('ending.wav'); // 게임이 종료되었을 때 승리 화면 출력 시 재생할 음악 파일
  let audio4 = new Audio('plz.m4a'); // 무르기 버튼을 눌렀을 때 재생할 소리 파일
  let audio5 = new Audio('oneMore.m4a'); // '한판 더' 버튼을 눌렀을 때 재생할 소리 파일

  // '한판 더' 버튼을 누르면 소리를 재생하고, 2초 후 페이지를 다시 로드하는 이벤트 핸들러
  btn1.addEventListener('mouseup', () => {
    audio5.play();
    setTimeout(() => {
      location.reload();
    }, 2000);
  });

  // 무르기 버튼을 누르면 소리를 재생하고, withdraw() 함수를 실행하는 이벤트 핸들러
  btn2.addEventListener('mouseup', () => {
    audio4.play();
    withdraw();
  });

  draw(); // 시작하면서 빈 오목판을 그리는 함수 호출

  // 배열을 콘솔창에 그리드 형태로 보여주는 함수. 디버깅 목적으로 사용되며 게임과 관련이 없습니다.
  function indexView(m) {
    let s = '\n';
    let c = 0;
    for (let e of m) {
      s += `${e} `;
      if (c % (row + 1) === row) s += '\n'; // 줄바꿈 문자 삽입
      c++;
    }
    return s;
  }

  // x, y 좌표를 배열의 인덱스 값으로 변환하는 함수
  let xyToIndex = (x, y) => {
    return x + y * (row + 1);
  };

  // 배열의 인덱스 값을 x, y 좌표로 변환하는 함수
  let indexToXy = (i) => {
    w = Math.sqrt(board.length);
    x = i % w;
    y = Math.floor(i / w);
    return [x, y];
  };

  // 오목판을 그리는 함수
  function draw() {
    ctx.fillStyle = '#e38d00'; // 바탕색 설정
    ctx.fillRect(0, 0, cw, ch); // 전체 캔버스를 바탕색으로 채움
    for (let x = 0; x < row; x++) {
      for (let y = 0; y < row; y++) {
        let w = (cw - margin * 2) / row;
        ctx.strokeStyle = 'black'; // 오목판 선 색상
        ctx.lineWidth = 1; // 오목판 선 두께
        ctx.strokeRect(w * x + margin, w * y + margin, w, w); // 오목판 그리기
      }
    }

    // 오목판의 화점에 점 찍기
    for (let a = 0; a < 3; a++) {
      for (let b = 0; b < 3; b++) {
        ctx.fillStyle = 'black';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(
          (3 + a) * rowSize + margin + a * 5 * rowSize,
          (3 + b) * rowSize + margin + b * 5 * rowSize,
          dolSize / 3,
          0,
          Math.PI * 2
        );
        ctx.fill();
      }
    }
  }

  // 방금 놓은 돌에 사각 표시를 그리는 함수
  drawRect = (x, y) => {
    let w = rowSize / 2;
    ctx.strokeStyle = 'red'; // 사각 표시 색상
    ctx.lineWidth = 3; // 사각 표시 두께
    ctx.strokeRect(
      x * rowSize + margin - w,
      y * rowSize + margin - w,
      w + rowSize / 2,
      w + rowSize / 2
    );
  };

  // 바둑돌을 그리는 함수. 사실 모든 오목판을 그리는 함수가 호출될 때마다 전체 오목판을 그립니다.
  drawCircle = (x, y) => {
    draw(); // 빈 오목판 그리기
    drawRect(x, y); // 방금 둔 돌에 사각 표시 그리기
    for (i = 0; i < board.length; i++) {
      // 모든 위치에 대해서 돌의 존재와 색상 확인
      let a = indexToXy(i)[0];
      let b = indexToXy(i)[1];

      if (board[xyToIndex(a, b)] == 1) {
        ctx.fillStyle = 'black'; // 흑돌 색상
        ctx.beginPath();
        ctx.arc(a * rowSize + margin, b * rowSize + margin, dolSize, 0, Math.PI * 2);
        ctx.fill();
      }
      if (board[xyToIndex(a, b)] == 2) {
        ctx.fillStyle = 'white'; // 백돌 색상
        ctx.beginPath();
        ctx.arc(a * rowSize + margin, b * rowSize + margin, dolSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    audio1.currentTime = 0.5; // 바둑돌 놓는 소리 파일을 0.5초 지점부터 재생
    audio1.play(); // 바둑돌 놓는 소리 재생

    checkWin(x, y); // 5개의 돌이 연속으로 놓였는지 확인하는 함수 실행

    let boardCopy = Object.assign([], board);
    history.push(boardCopy); // 현재 전체 오목판 모양을 배열에 저장하여 무르기 기능을 위해 사용
  };

  // 무르기 기능 구현 함수
  withdraw = () => {
    history.pop(); // 최근에 놓인 돌을 되돌리면서 배열에서 제거
    lastBoard = history.slice(-1)[0]; // 가장 최근의 오목판 모양 저장
    board = lastBoard;
    count--; // 흑돌과 백돌의 무르기 횟수 줄이기

    draw(); // 오목판을 다시 그림

    // 이전 오목판 모양에 따라 흑돌과 백돌을 다시 그림
    for (i = 0; i < lastBoard.length; i++) {
      let a = indexToXy(i)[0];
      let b = indexToXy(i)[1];

      if (lastBoard[xyToIndex(a, b)] == 1) {
        ctx.fillStyle = 'black';
        ctx.beginPath();
        ctx.arc(a * rowSize + margin, b * rowSize + margin, dolSize, 0, Math.PI * 2);
        ctx.fill();
      }
      if (lastBoard[xyToIndex(a, b)] == 2) {
        ctx.fillStyle = 'white';
        ctx.beginPath();
        ctx.arc(a * rowSize + margin, b * rowSize + margin, dolSize, 0, Math.PI * 2);
        ctx.fill();
      }
    }
  };

  // 승리 여부를 확인하는 함수
  function checkWin(x, y) {
    let thisColor = board[xyToIndex(x, y)]; // 방금 둔 돌의 색깔(1: 흑돌, 2: 백돌)
    // 모든 방향(수직, 수평, 대각선)으로 5개의 돌이 연속으로 놓여 있는지 확인
    for (k = 0; k < 4; k++) {
      winBlack = 1; winWhite = 1;
      // 둔 돌 기준 양 방향으로 확인
      for (j = 0; j < 2; j++) {
        // 5개의 돌의 색상을 확인
        for (i = 1; i < 5; i++) {
          let a = x + checkDirection[k + 4 * j][0] * i;
          let b = y + checkDirection[k + 4 * j][1] * i;
          if (board[xyToIndex(a, b)] == thisColor) {
            // 돌의 색에 따라 흑돌과 백돌의 개수 증가
            switch (thisColor) {
              case 1: winBlack++; break;
              case 2: winWhite++; break;
            }
          } else { break; }
        }
      }
      // 5개의 돌이 연속으로 놓여있으면 승리 화면 표시
      if (winBlack == 5) { winShow(1); }
      if (winWhite == 5) { winShow(2); }
    }
  } // 승리 여부 확인 함수의 끝

  // 승리 화면을 표시하는 함수
  function winShow(x) {
    audio3.play();
    switch (x) {
      case 1:
        // 음악이 재생되기 위해 약간의 지연 후 화면을 표시
        setTimeout(() => {
          blackWinScreen.style.visibility = 'visible';
          blackWinScreen.style.zIndex = 2;
          const troImg = document.querySelector('#trophyImg');
          troImg.style.animationName = 'trophy';
        }, 300);
        break;
      case 2:
        // 음악이 재생되기 위해 약간의 지연 후 화면을 표시
        setTimeout(() => {
          whiteWinScreen.style.visibility = 'visible';
          whiteWinScreen.style.zIndex = 2;
          const troImg = document.querySelector('#trophyImg2');
          troImg.style.animationName = 'trophy';
        }, 300);
        break;
    }
  }

  // 마우스로 클릭한 위치를 정확한 오목판 좌표로 보정하는 이벤트 핸들러
  document.addEventListener('mouseup', (e) => {
    if (e.target.id == 'canvas') {
      let x = Math.round(Math.abs(e.offsetX - margin) / rowSize);
      let y = Math.round(Math.abs(e.offsetY - margin) / rowSize);
      console.log(e.offsetX, e.offsetY, x, y);
      if (
        e.offsetX > 10 &&
        e.offsetX < 640 &&
        e.offsetY > 10 &&
        e.offsetY < 640
      ) {
        // 이미 돌이 놓여져 있으면 경고 소리 재생
        if (board[xyToIndex(x, y)] != -1) {
          audio2.play();
        } else {
          // 빈 자리인 경우, 순서에 따라 흑돌 또는 백돌을 놓는 함수 실행
          count % 2 == 0
            ? (board[xyToIndex(x, y)] = 1)
            : (board[xyToIndex(x, y)] = 2);
          count++;
          drawCircle(x, y); // 바둑돌을 놓는 함수 호출
        }
      }
    }
  });
};

```

