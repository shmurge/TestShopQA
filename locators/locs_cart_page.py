class CartPageLocators:
    ORDER_OVERVIEW = ('css selector', '[class="mb-4"]')
    EMPTY_CART_MESSAGE = ('css selector', '[class="js_cart_lines alert alert-info"]')
    PRODUCT_TITLE = ('xpath', '//*[contains(@class, "d-inline align-top")]')
    PRODUCT_PRICE = ('css selector', '[data-oe-expression="product_price"]')
    QUANTITY_INPUT = ('css selector', '[class="css_quantity input-group mb-2"] [type="text"]')

    SUBTOTAL_PRICE = ('css selector', '[id="order_total_untaxed"] [class="monetary_field"]')
    TAXES = ('css selector', '[id="order_total_taxes"] [class="monetary_field"]')
    TOTAL_PRICE = ('css selector', '[class="monetary_field text-end p-0"]')

    DELETE_PRODUCT_BUTTON = ('css selector', '[title="Remove from cart"]')
