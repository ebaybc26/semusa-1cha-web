# -*- coding: utf-8 -*-
"""
semusa-1cha-study 저장소의 webapp/index.html(Artifact 본문)을
GitHub Pages용 완전한 HTML 문서로 감싸서 index.html을 생성한다.

Artifact로 발행할 때는 claude.ai가 doctype/head/viewport를 자동으로 붙여주지만,
GitHub Pages는 파일을 그대로 서빙하므로 직접 감싸주지 않으면
휴대폰에서 뷰포트가 980px로 잡혀 화면이 축소된다.

사용법:  python build.py [원본경로]
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SRC = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\alsrb\semusa-1cha-study\webapp\index.html'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

body = open(SRC, encoding='utf-8').read()

HEAD = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="세무사 1차 시험 기출 479문항(2023·2024·2025) 과목·단원별 문제풀이">
<meta name="color-scheme" content="light dark">
<meta name="format-detection" content="telephone=no">
<style>
  *{box-sizing:border-box}
  html,body{margin:0;padding:0}
  img{max-width:100%}
</style>
</head>
<body>
'''
FOOT = '\n</body>\n</html>\n'

open(OUT, 'w', encoding='utf-8', newline='').write(HEAD + body + FOOT)
print('생성 완료:', OUT)
print('  원본 %d bytes → 출력 %d bytes' % (len(body), len(HEAD)+len(body)+len(FOOT)))
