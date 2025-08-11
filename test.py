import requests
import datetime
import json

def fetch_and_save_todo():
    """
    현재 시간을 기준으로 'jsonplaceholder' API에서 데이터를 가져와 
    'test.json' 파일로 저장하는 함수
    """
    try:
        # 1. 현재 시간의 '분'을 가져와 1을 더함
        current_minute = datetime.datetime.now().minute
        target_id = current_minute + 1
        
        # 2. API URL 구성
        api_url = f"https://jsonplaceholder.typicode.com/todos/{target_id}"
        print(f"데이터를 요청할 URL: {api_url}")
        
        # 3. requests 라이브러리를 사용해 API에 GET 요청
        response = requests.get(api_url)
        # HTTP 에러(404, 500 등)가 발생하면 예외를 발생시킴
        response.raise_for_status()
        
        # 4. 응답받은 데이터를 JSON 형식으로 변환
        data = response.json()
        
        # 5. 'test.json' 파일에 예쁘게 포맷팅하여 저장 (utf-8 인코딩)
        #    indent=4 : 보기 좋게 4칸 들여쓰기
        with open('test.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        print(f"성공! 'test.json' 파일이 현재 디렉토리에 저장되었습니다.")

    except requests.exceptions.RequestException as e:
        # 네트워크 오류 또는 HTTP 에러 처리
        print(f"오류 발생: API 요청에 실패했습니다. ({e})")
    except Exception as e:
        # 기타 예상치 못한 오류 처리
        print(f"알 수 없는 오류가 발생했습니다: {e}")

# 스크립트가 직접 실행될 때 fetch_and_save_todo 함수를 호출
if __name__ == "__main__":
    fetch_and_save_todo()