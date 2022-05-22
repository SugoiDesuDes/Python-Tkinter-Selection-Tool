#top_left and bottom_right are PERCENTAGES of the max width / height of the given pdf 
class SelectedRegion:
    pdf_name = ""
    top_left = 0
    bottom_right = 0

    def __init__(self):
        self.top_left = 0
        self.bottom_right = 0

    def __str__(self):
        return(f"pdf: {self.pdf_name}\ntop_left: {self.top_left} \nbottom_right: {self.bottom_right}")