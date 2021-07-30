# 제작일: 2021년 7월 30일
# 참고자료: Biopython Tutorial and Cookbook(1.77)
# 웹페이지: http://biopython.org/DIST/docs/tutorial/Tutorial.html

# 기본 사용법
from Bio.Seq import Seq

my_seq = Seq("AGCTAAATTCAGGGACACACT")

print(my_seq)