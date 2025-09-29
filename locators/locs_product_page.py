class ProductPageLocators:
    PRODUCT_TITLE = ('css selector', '[itemprop="name"]')
    PRODUCT_PRICE = ('css selector', '[class="oe_price"]')
    ADD_TO_CART_BUTTON = ('css selector', '[id="add_to_cart"]')
    ADD_ONE_BUTTON = ('css selector', '[id="o_wsale_cta_wrapper"] [title="Add one"]')
    REMOVE_ONE_BUTTON = ('css selector', '[id="o_wsale_cta_wrapper"] [title="Remove one"]')
    QUANTITY_INPUT = ('css selector', '[id="o_wsale_cta_wrapper"] [name="add_qty"]')

    RADIO_BUTTON_MATERIAL = ('css selector', '[type="radio"][data-attribute_name="Legs"]')
    RADIO_BUTTON_STEEL = ('css selector', '[type="radio"][data-value_name="Steel"]')
    RADIO_BUTTON_ALUMINIUM = ('css selector', '[type="radio"][data-value_name="Aluminium"]')
    RADIO_BUTTON_CUSTOM = ('css selector', '[type="radio"][data-value_name="Custom"]')
    INPUT_CUSTOM = ('css selector', '[data-attribute_value_name="Custom"]')

    RADIO_BUTTON_COLOR = ('css selector', '[type="radio"][data-attribute_name="Color"]')
    RADIO_BUTTON_BLACK = ('css selector', '[style="background:#000000"]')
    RADIO_BUTTON_WHITE = ('css selector', '[style="background:#FFFFFF"]')

    PRODUCT_DESCRIPTION = ('xpath', '//*[contains(@placeholder, "A short description")]')

    CUSTOMIZE_DESK_PHOTO_ALUM_WHITE = ('xpath', '//*[contains(@src, "/web/image/product.product/14/")]')
    CUSTOMIZE_DESK_PHOTO_STEEL_BLACK = ('xpath', '//*[contains(@src, "/web/image/product.product/13/")]')
    CUSTOMIZE_DESK_PHOTO_STEEL_WHITE = ('xpath', '//*[contains(@src, "/web/image/product.product/12/")]')
