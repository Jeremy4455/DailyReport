import urllib3
from selenium.webdriver import Edge
from time import sleep

urllib3.disable_warnings()

student_id = ""
password = ""
driver = Edge()


def login():
    driver.maximize_window()
    driver.get("https://selfreport.shu.edu.cn/")
    script = "Object.defineProperty(navigator, 'webdriver', {get:()=>undefined, });"
    driver.execute_script(script)
    sleep(1)
    input_student_id = driver.find_element(by="css selector", value="#username")
    input_student_id.click()
    input_student_id.send_keys(student_id)
    sleep(2)
    input_password = driver.find_element(by="css selector", value="#password")
    input_password.click()
    input_password.send_keys(password)
    sleep(2)
    driver.find_element(by="css selector", value="#submit-button").click()
    sleep(3)
    return


def report(day):
    driver.get(f"https://selfreport.shu.edu.cn/DayReport.aspx?day={day}")
    prom_butt = driver.find_element(by="css selector", value="#p1_ChengNuo-inputEl-icon")
    prom_butt.click()
    sleep(2)
    driver.find_element(by="css selector", value="#fineui_1-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_9-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_12-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_16-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_18-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_27-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_28-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_33-inputEl-icon").click()
    sleep(1)
    driver.find_element(by="css selector", value="#p1_ctl01_btnSubmit > span > span").click()
    sleep(1)
    driver.find_element(by="css selector", value="#fineui_41").click()
    sleep(2)
    return


def check():
    login()
    driver.get("https://selfreport.shu.edu.cn/ReportHistory.aspx")
    days = driver.find_elements(by="css selector", value="ul[class='f-datalist-list'] li")
    need_reports = []
    for day in days:
        strlist = day.text.split('(')
        if strlist[1][:1] != '???':
            need_reports.append(strlist[0])
    need_reports.reverse()
    for need_report in need_reports:
        print(need_report+"????????????")
        report(need_report)
    if not need_reports:
        print("???????????????")
    else:
        print("???????????????")


if __name__ == "__main__":
    check()
