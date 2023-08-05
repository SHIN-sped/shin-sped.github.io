---
title: "[NIPA]AI+웹개발 취업캠프 SW기초 1주차 2회"
excerpt: "데일리 제출"

categories:
  - Categories1
tags:
  - [정보통신산업진흥원, NIPA, AI교육, 프로젝트, 유데미, IT개발캠프, 개발자부트캠프, 프론트엔드, 백엔드, AI웹개발취업캠프, 취업캠프, 개발취업캠프]

permalink: /categories1/post-name-here-2/

toc: true
toc_sticky: true

date: 2023-07-19
last_modified_at: 2023-07-19
---

## 😀 본문
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

### 코드리뷰

1. **의미 있는 HTML 태그**: HTML 구조에 의미 있는 요소가 부족합니다. 웹사이트의 구조와 접근성을 향상시키기 위해 `<header>`, `<main>`, `<article>`, `<section>`, 그리고 `<footer>`와 같은 HTML5 시맨틱 태그를 사용하는 것이 중요합니다.

2. **올바른 URL**: 첫 번째 `<section>` 내부의 `<a>` 태그에 빈 `href` 속성이 있습니다 (`<a hre="">`). 이 링크들에 올바른 URL을 제공해야 합니다.

3. **중복된 <main> 요소**: 코드에 `<main>` 요소가 두 개 있습니다. 올바른 구조를 위해 페이지에는 한 개의 `<main>` 요소만 존재해야 합니다.

4. **위치가 잘못된 콘텐츠**: 앨범 소개와 "앨범에 대해" 섹션 등 일부 콘텐츠가 `<a>` 태그 내부에 있습니다. 링크는 주로 탐색을 위해 사용되어야 하며, 대신 `<div>`나 `<article>`과 같은 요소를 사용하여 콘텐츠 블록을 나타내야 합니다.

5. **CSS 스타일링**: 코드에 일부 인라인 CSS 스타일 (`style` 속성)이 있습니다. 유지보수와 가독성을 위해 CSS를 별도의 스타일 시트로 분리하는 것이 좋습니다.

6. **접근성**: 이미지에 적절한 `alt` 속성을 제공하고 접근성을 위한 최선의 방법을 따르는 것이 중요합니다.

7. **반응형 디자인**: 코드에 반응형 디자인 요소가 없습니다. 미디어 쿼리와 CSS 플렉스박스/그리드를 사용하여 다양한 화면 크기에서 잘 동작하는 반응형 레이아웃을 구축해야 합니다.

8. **콘텐츠**: 현재 "didididi"나 "앨범 소개"와 같은 대부분의 콘텐츠는 임시 데이터로 채워져 있습니다. 완성된 웹사이트를 위해 실제와 관련성 있는 콘텐츠로 대체해야 합니다.

   ​

### 부족한 점

1. **시맨틱 HTML**: HTML 구조에 시맨틱 요소가 없습니다. `<header>`, `<main>`, `<article>`, `<section>` 및 `<footer>`와 같은 적절한 HTML5 시맨틱 태그를 사용하여 웹사이트의 전체 구조와 접근성을 개선하는 것이 필수적입니다. .
2. **적절한 URL**: 첫 번째 `<section>` 내부의 `<a>` 태그에는 빈 `href` 속성(`<a hre="">`)이 있습니다. 이러한 링크에 대해 유효한 URL을 제공해야 합니다.
3. **중복 <main> 요소**: 코드에 잘못된 `<main>` 요소가 두 개 있습니다. 메인 콘텐츠를 나타내기 위해 하나의 `<main>` 요소만 페이지에 있어야 합니다.
4. **잘못 배치된 콘텐츠**: 앨범 소개 및 "앨범 정보" 섹션과 같은 일부 콘텐츠는 `<a>` 태그 안에 있습니다. 링크는 일반적으로 탐색 목적으로 사용해야 합니다. 대신 `<div>` 또는 `<article>`과 같은 적절한 요소를 사용하여 콘텐츠 블록을 나타냅니다.
5. **CSS 스타일링**: 코드에 일부 인라인 CSS 스타일(`style` 속성)이 있습니다. 더 쉬운 유지 관리와 가독성을 위해 CSS를 별도의 스타일시트로 분리하는 것이 좋습니다.
6. **접근성**: 이미지에 적절한 'alt' 속성을 제공하고 접근성 모범 사례를 따르도록 합니다.
7. **반응형 디자인**: 코드에 반응형 디자인 요소가 없습니다. 미디어 쿼리와 CSS flexbox/grid를 사용하여 다양한 화면 크기에서 잘 작동하는 반응형 레이아웃을 만드세요.
8. **콘텐츠**: 현재 대부분의 콘텐츠는 "디디디디", "앨범 소개"와 같은 자리 표시자입니다. 완전한 웹사이트를 위해서는 실제 관련 콘텐츠로 채워야 합니다.



  본 후기는 정보통신산업진흥원(NIPA)에서 주관하는 <AI 서비스 완성! AI+웹개발 취업캠프 - 프론트엔드&백엔드> 과정 학습/프로젝트/과제 기록으로 작성 되었습니다. #정보통신산업진흥원 #NIPA #AI교육 #프로젝트 #유데미 #IT개발캠프 #개발자부트캠프 #프론트엔드 #백엔드 #AI웹개발취업캠프 #취업캠프 #개발취업캠프   
