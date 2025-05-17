from django import template

register = template.Library()

@register.filter
def get_smart_page_range(paginator, page_obj, num_pages_to_show=5):
    # Calculate the start and end page numbers to show around the current page
    start_page = max(1, page_obj.number - (num_pages_to_show // 2))
    end_page = min(paginator.num_pages, page_obj.number + (num_pages_to_show // 2))

    # Adjust start and end if we are near the beginning or end
    if end_page - start_page < num_pages_to_show - 1:
        if start_page == 1:
            end_page = min(paginator.num_pages, start_page + num_pages_to_show - 1)
        elif end_page == paginator.num_pages:
            start_page = max(1, end_page - num_pages_to_show + 1)

    page_range = list(range(start_page, end_page + 1))

    # Add ellipses and first/last pages if needed
    if 1 not in page_range:
        page_range.insert(0, 1)
        if 2 not in page_range:
            page_range.insert(1, '...')

    if paginator.num_pages not in page_range:
        if paginator.num_pages not in page_range:
             if paginator.num_pages - 1 not in page_range:
                 page_range.append('...')
        page_range.append(paginator.num_pages)

    return page_range
