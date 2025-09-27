class ModalAddToCartLocators:
    PRODUCT_TITLE = ('xpath', '//*[contains(@class, "js_product in_cart")]/descendant::strong')
    PRODUCT_PRICE = ('xpath', '//*[contains(@class, "js_product in_cart")]/descendant::*[@class="oe_price product_id"]')
    TOTAL_PRICE = ('css selector', '[class="js_price_total fw-bold"]')

    ADD_TO_CART_MODAL = ('css selector', '[class="modal-content"]')
    ADD_ONE_BUTTON = ('css selector', '[class="text-center td-qty"] [title="Add one"]')
    REMOVE_ONE_BUTTON = ('css selector', '[class="text-center td-qty"] [title="Remove one"]')
    QUANTITY_INPUT = ('css selector', '[class="text-center td-qty"] [name="add_qty"]')
    CLOSE_ADD_TO_CART_MODAL_BUTTON = ('css selector', '[class="modal-content"] [aria-label="Close"]')

    CONTINUE_SHOPPING_BUTTON = ('xpath', '//*[@class="btn btn-secondary"]')
    PROCEED_TO_CHECKOUT_BUTTON = ('xpath', '//*[contains(@class, "btn btn-primary o_sa")]')
