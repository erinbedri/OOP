from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4
    SEPARATOR_COUNT = 11

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__create_album(self.pages)

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for page_index in range(len(self.photos)):
            page = self.photos[page_index]
            if len(page) < PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                self.photos[page_index].append(label)
                return f"{label} photo added successfully on page " \
                       f"{page_index + 1} slot {len(self.photos[page_index])}"
        return "No more free slots"

    def display(self):
        separator = "-" * PhotoAlbum.SEPARATOR_COUNT
        result = separator + "\n"
        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + "\n"
            result += separator + "\n"
        return result.strip()

    @staticmethod
    def __create_album(pages):
        temp_album = []
        for _ in range(pages):
            page = []
            temp_album.append(page)
        return temp_album