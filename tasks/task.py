import math
class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.page_count = self.page_count()
        self.item_count = len(self.data)

    def page_count(self):
        return math.ceil(len(self.data) / self.items_on_page)

    def count_items_on_page(self, page_number):
        try:
            if page_number < self.page_count:
                num = (page_number + 1) * self.items_on_page
                if self.item_count - num >= 0:
                    return self.items_on_page
                else:
                    return self.items_on_page + (self.item_count - num)
            else:
                raise Exception('Invalid index. Page is missing.')
        except Exception as e:
            print(e)

    def find_page(self, data):
        list = self.get_pages_items()
        new_set = set()
        list_of_c = []
        new_list = []
        new_ind = 0
        while new_ind < self.item_count:
            i = self.data.find(data, new_ind)
            if i != -1:
                list_of_c.append(i)
            else:
                break
            new_ind = i + 1
        if len(list_of_c) == 1:
            start_ind = self.data.find(data)
            end_ind = self.data.rfind(data[-1])
            new_set.add(start_ind // self.items_on_page)
            new_set.add(end_ind // self.items_on_page)
        else:
            for i in list_of_c:
                new_set.add(i // self.items_on_page )
        for i in new_set:
            new_list.append(i)
        try:
            if new_list == []:
                raise Exception(data, ' is missing on the pages')
        except Exception as e:
            print(e)
        return new_list

    def display_page(self, page_number):
        list = self.get_pages_items()
        return list[page_number]

    def get_pages_items(self):
        new_list = []
        prev_ind = 0
        new_word = ''
        for i in range(1, self.page_count):
            new_word += self.data[prev_ind:i*self.items_on_page]
            prev_ind = i*self.items_on_page
            new_list.append(new_word)
            new_word = ''
        if prev_ind < self.item_count:
            new_list.append(self.data[prev_ind:self.item_count])
        return new_list

