class PagesDataStore(object):

    def __init__(self, db):
        self.db = db

    def add_link_to_crawl(self, url):
        """link_to_crawl에 지정된 링크를 추가한다."""

    def remove_link_to_crawl(self, url):
        """links_to_crawl에서 해당 링크를 제거한다."""

    def reduce_priority_link_to_crawl(self, url):
        """루프를 방지하기 위해 link_to_crawl의 링크 우선순위를 낮춘다."""

    def extract_max_priority_page(self):
        """link_to_crawl에서 우선순위가 가장 높은 링크를 반환한다."""

    def insert_crawled_link(self, url, signature):
        """crawled_links에 지정된 링크를 추가한다."""

    def crawled_similar(self, signature):
        """특정 서명과 일치하는 페이지가 크롤링되었는지 확인"""
