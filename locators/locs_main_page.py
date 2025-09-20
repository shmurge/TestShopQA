class MainPageLocators:
    SEARCH_INPUT = ('css selector', '[id="products_grid"] [name="search"]')

    MESSAGE_ON_PAGE_NO_SEARCHING_RESULTS = ('xpath', '//*[contains(@class, "text-center text-muted")]')
    SEARCHING_RESULT_CNT = ('xpath', '//*[contains(@class, "products_header")]/descendant::*[@class="oe_search_found"]')

    PRODUCT_TITLE = ('css selector', '[itemprop="name"]')
    PRODUCT_PRICE = ('css selector', '[class="product_price"]')
