def solution(genres, plays):
    answer = []
    
    # 1. 데이터 구조 만들기
    # genre_total: {장르: 총 재생수}
    # genre_songs: {장르: [(재생수, 고유번호), ...]}
    genre_total = {}
    genre_songs = {}
    
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        
        # 장르별 총합 누적
        genre_total[g] = genre_total.get(g, 0) + p
        
        # 장르별 곡 정보 저장
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((p, i))

    # 2. 장르 총 재생 횟수 내림차순 정렬
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)

    # 3. 각 장르 내에서 곡 정렬 후 최대 2개 추출
    for genre, total in sorted_genres:
        # 장르 내 곡 정렬 기준:
        # 1순위: 재생 횟수(x[0]) 내림차순 (-)
        # 2순위: 고유 번호(x[1]) 오름차순 (+)
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # 최대 2개까지 정답 리스트에 추가
        answer.extend([s[1] for s in songs[:2]])

    return answer