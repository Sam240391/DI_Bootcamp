class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items or []
        self.pageSize = pageSize
        self.current_page = 1
        self.total_pages = (len(self.items) + self.pageSize - 1) // self.pageSize

    def get_total_page(self):
        result = (len(self.items) + self.pageSize - 1) // self.pageSize
        print(result)


    def getVisibleItems(self):
        start = (self.current_page - 1) * self.pageSize
        end = self.current_page * self.pageSize
        return self.items[start:end]

    
    def prevPage(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def nextPage(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def firstPage(self):
        self.current_page = 1
        return self

    def lastPage(self):
        self.current_page = self.total_pages
        return self

    def goToPage(self, page_num):
        if page_num <= 0:
            self.current_page = 1
        elif page_num > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = page_num
        return self



alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4) 

p.get_total_page()


print(p.getVisibleItems())

p.nextPage()

print(p.getVisibleItems())

p.lastPage()

print(p.getVisibleItems())

p.prevPage()

print(p.getVisibleItems())
