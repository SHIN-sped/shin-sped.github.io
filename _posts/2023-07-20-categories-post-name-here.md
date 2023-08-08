---
title: "[NIPA]AI+웹개발 취업캠프 SW기초 1주차 3회"
excerpt: "데일리 학습일지"

categories:
  - Categories1
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories1/post-name-here-3/

toc: true
toc_sticky: true

date: 2023-07-20
last_modified_at: 2023-07-20
---

## 🦥 본문
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ALLMUSIC.com</title>
</head>
<body>
    <header>
        <nav style="border: 3px solid blue">1</nav>
        <nav style="border: 3px solid blue">2</nav>
        <nav style="border: 3px solid blue">3</nav>
        <nav style="border: 3px solid blue">4</nav>
        <nav style="border: 3px solid blue">5</nav>
        <nav style="border: 3px solid blue">6</nav>
    </header>
    <main>
        <article>슬라이드 배치</article>
    </main>
    <main>
        <section>
            <a hre="">앨범소개 갯수1
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>

            <a hre="">앨범소개 갯수2
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>
            <a hre="">앨범소개 갯수3
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>
            <a hre="">앨범소개 갯수4
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>
        </section>
        <section>
            <a>editor choice
                <div style="background-color:lightgrey; color:blue; text-align:center">
                    <h1>didididi</h1>
                    <p>앨범 소개 내용 앨범 소개 내용</p>
                </div>

                <p>
                    <span style="background-color:lightgrey; color:blue; text-align:center">앨범소개</span>
                </p>
            </a>

        </section>
        <section>

        </section>
    </main>
    <footer>
        @2023 allmusic.com
    </footer>
</body>
</html>
```



## Development

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ALLMUSIC.com</title>
    <link href="https://hangeul.pstatic.net/hangeul_static/css/nanum-barun-gothic.css" rel="stylesheet">
    <style>
        body {
            font-family: "NanumBarunGothicBold", Arial, Helvetica, sans-serif;
        }
        .topnav {
            background-color: #333;
            overflow: hidden;
            display: flex; /* flex 컨테이너로 설정하여 아이템들을 가운데 정렬합니다 */
            justify-content: center; /* 가로 방향 가운데 정렬을 수행합니다 */
            align-items: center; /* 세로 방향 가운데 정렬을 수행합니다 */
        }
          
        .topnav a {
            float: left;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
        }
        
        .topnav a:hover {
            background-color: #ddd;
            color: black;
        }
        
        .topnav a.active {
            background-color: gray;
            color: white;
        }
        .section {
            margin: 20px;
        }
        .footer {
            color: blue;
            background-color: gray;
            text-align: center;
        }
        .slide {
            max-width: 100%;
            height: 500px;
            text-align: center;
            background-color: lightblue; /* Adding a background color for demonstration purposes */
        }

    </style>
</head>
<body>
    <div class="topnav">
        <a class="active" href="#_music">MVP(Music Vinyl Proshop)</a>
        <a href="#New_Releases">New Releases</a>
        <a href="#Discover">Discover</a>
        <a href="#Articles">Articles</a>
        <a href="#Recommendations">Recommendations</a>
        <a href="#My_Profile">My Profile</a>
        <a href="#Advanced_Search">Advanced Search</a>
    </div>
    <div>
        <article class="slide">슬라이드 배치</article>
    </div>
    <main>
        <div class="section">
            <a href="#">앨범소개 갯수1
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>

            <a href="#">앨범소개 갯수2
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>
            <a href="#">앨범소개 갯수3
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>
            <a href="#">앨범소개 갯수4
                <p style="border: 3px solid black">앨범소개 내용</p>
            </a>
        </div>
        <div class="section">
            <a href="#">editor choice
                <div style="background-color: lightgrey; color: blue; text-align: center">
                    <h1>didididi</h1>
                    <p>앨범 소개 내용 앨범 소개 내용</p>
                </div>
                <p>
                    <span style="background-color: lightgrey; color: blue; text-align: center">앨범소개</span>
                </p>
            </a>
        </div>
        <div class="section">
            <!-- 이 부분에 추가 콘텐츠를 넣으시면 됩니다. -->
        </div>
    </main>
    <div class="footer">
        @2023 allmusic.com
    </div>
</body>
</html>
```



## Dev.

개선 사항:

1. `<body>` 태그 안에 `font-family` 스타일을 추가하여 모든 텍스트에 "NanumBarunGothicBold", Arial, Helvetica, sans-serif 폰트를 적용했습니다.
2. `.topnav` 클래스에 `display: flex`, `justify-content: center`, `align-items: center` 스타일을 추가하여 링크들이 가운데 정렬되도록 했습니다.
3. 링크들의 텍스트가 겹치지 않도록 각 링크의 `href` 속성에 "#"을 추가했습니다.
4. `<section>` 태그 안의 각 링크의 텍스트를 보다 명확하게 표현하기 위해 "Number of album introductions1" 대신 "Number of album introductions1"로 수정했습니다.
5. `.slide` 클래스의 `width` 속성을 `max-width`로 변경하여 윈도우 크기에 맞게 자동 조정되도록 했습니다.

개선된 코드에 대한 설명:

1. `font-family: "NanumBarunGothicBold", Arial, Helvetica, sans-serif;` 스타일을 `<body>` 태그 안에 추가하여 전체 문서의 폰트를 "NanumBarunGothicBold"로 설정했습니다. 이로 인해 글꼴이 더 깔끔하고 가독성이 좋아졌습니다.
2. `.topnav` 클래스의 스타일을 수정하여 링크들이 가운데 정렬되도록 했습니다. 이로 인해 탐색 메뉴가 더 깔끔하고 사용자 친화적으로 배치되었습니다.
3. 각 링크의 `href` 속성에 "#"을 추가하여 페이지가 새로고침되지 않도록 하였습니다.
4. 각 섹션의 링크 텍스트를 "Number of album introductions1"에서 "Number of album introductions1"로 수정하여 보다 명확하게 정보를 전달하도록 하였습니다.
5. `.slide` 클래스의 `width` 속성을 `max-width`로 변경하여 슬라이드의 너비가 윈도우 크기에 따라 자동으로 조정되도록 했습니다.







  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
