# 집합 (set)
# 세트는 중복을 허용하지 않는다
# 세트는 순서가 없다

set1 = {1,2,3,3,3}
print(set1)

무한도전 = {"유재석", "박명수", "정준하", "노홍철", "하하"}
런닝맨 = set(["유재석", "하하", "김종국", "송지효", "이광수"])

# 교집합 출력
print(무한도전 & 런닝맨)
print(무한도전.intersection(런닝맨))

# 합집합
print(무한도전 | 런닝맨)
print(무한도전.union(런닝맨))

# 차집합
print(무한도전 - 런닝맨)
print(무한도전.difference(런닝맨))

# 무한도전 멤버 추가
무한도전.add("서장훈")
print(무한도전)

# 무한도전 멤버 탈퇴
무한도전.remove("유재석")
print(무한도전)