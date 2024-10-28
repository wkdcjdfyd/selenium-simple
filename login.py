from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


MY_ID = "YOUR_ID"
MY_PW = "YOUR_PW"
URL = "TARGET_URL"


def try_login(driver, id: str, pw: str):
    try:
        # 사용자 아이디 입력
        id_input = driver.find_element(By.ID, "id")
        id_input.send_keys(id)

        # 비밀번호 입력
        pw_input = driver.find_element(By.ID, "pw")
        pw_input.send_keys(pw)

        # 로그인 시도
        login_submit_btn = driver.find_element(By.ID, "loginBtn")
        login_submit_btn.click()

    except NoSuchElementException as e:
        auth_login_submit_btn = driver.find_element(By.ID, "autoOauthLogin")
        auth_login_submit_btn.click()


if __name__ == "__main__":
    options = Options()
    options.add_argument('window-size=1920x1080')
    options.add_argument('--start-maximized')
    options.add_experimental_option("detach", True)

    # 불필요한 에러메시지 노출 방지
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options)
    driver.get(URL)

    # 로그인 화면 열기
    login_button = driver.find_element(By.ID, "loginBtn")
    login_button.click()

    # 현재 열린 모든 창 핸들 가져오기
    main_window = driver.current_window_handle
    all_windows = driver.window_handles

    for window in all_windows:
        if window != main_window:
            # 로그인 화면으로 전환
            driver.switch_to.window(window)

            # 로그인 시도
            try_login(driver, MY_ID, MY_PW)

            # 메인 화면으로 전환
            driver.switch_to.window(main_window)
            break