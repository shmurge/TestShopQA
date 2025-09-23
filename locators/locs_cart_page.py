class CartPageLocators:
    ORDER_OVERVIEW = ('css selector', '[class="mb-4"]')
    EMPTY_CART_MESSAGE = ('css selector', '[class="js_cart_lines alert alert-info"]')
    PRODUCT_TITLE = ('xpath', '//*[contains(@class, "d-inline align-top")]')
    PRODUCT_PRICE = ('css selector', '[data-oe-expression="product_price"]')
    QUANTITY_INPUT = ('css selector', '[class="css_quantity input-group mb-2"] [type="text"]')
