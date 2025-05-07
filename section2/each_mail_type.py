from collections import defaultdict

class interviewUtility:
    @staticmethod
    def required_info_for_document_rejection():
        required_info = defaultdict()
        required_info['receiver_name'] = input("이메일 받는 사람 이름: ")
        required_info['job_title'] = input("채용 공고명: ")
        required_info['your_company_name'] = input("회사명: ")
        return required_info
    
    @staticmethod
    def required_info_for_interview_rejection():
        required_info = defaultdict()
        required_info['receiver_name'] = input("이메일 받는 사람 이름: ")
        required_info['job_title'] = input("채용 공고명: ")
        required_info['your_company_name'] = input("회사명: ")
        return required_info

    @staticmethod
    def required_info_for_first_interview():
        required_info = defaultdict()
        required_info['receiver_name'] = input("이메일 받는 사람 이름: ")
        required_info['job_title'] = input("채용 공고명: ")
        required_info['recruitment_stage'] = input("몇차 채용인지 (1\2): ")
        required_info['interview_date'] = input("다음 인터뷰 날짜: ")
        required_info['your_company_name'] = input("회사명: ")
        return required_info
    
    @staticmethod
    def required_info_for_second_interview():
        required_info = defaultdict()
        required_info['receiver_name'] = input("이메일 받는 사람 이름: ")
        required_info['job_title'] = input("채용 공고명: ")
        required_info['recruitment_stage'] = input("몇차 채용인지 (1\2): ")
        required_info['interview_date'] = input("다음 인터뷰 날짜: ")
        required_info['your_company_name'] = input("회사명: ")
        return required_info