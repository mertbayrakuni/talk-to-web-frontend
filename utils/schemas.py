from django.utils.translation import gettext as _
from drf_yasg import openapi

broker_group_toggle_response_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    200: openapi.Response(
        description="Bayi Grup response",
        examples={
            "application/json": {
                "success": True,
                "message": ""
            }
        }
    ),
}

broker_code_name_id_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    200: openapi.Response(
        description="Bayi İsim-Kod-ID",
        examples={
            "application/json": {
                "success": True,
                "message": ""
            }
        }
    ),
}
wishlist_toggle_response_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    200: openapi.Response(
        description="WishList Toggle (Follow/Unfollow Propduct)",
        examples={
            "application/json": {
                "success": True,
                "message": ""
            }
        }
    ),
}

application_action_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    200: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                "stutus": "success",
                "message": "Product specs and variants are updated"
            }
        }
    )
}

set_password_request_dict = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        "password":  openapi.Schema(type=openapi.TYPE_STRING, description='string: ****'),
        "re_password":  openapi.Schema(type=openapi.TYPE_STRING, description='string: ****'),
    }
)
set_password_response_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    200: openapi.Response(
        description="Set user new password",
        examples={
            "application/json": {
                 "status": "success",
                 "title": "Şİfre başarı ile değiştirildi.",
            }
        }
    )
}
makbuz_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    200: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                 "id": "883",
                 "original": "https://panel.guvenassist.com",
                 "title": "Makbuz Title",
            }
        }
    )
}
sozlesme_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    200: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                 "id": "883",
                 "original": "https://panel.guvenassist.com",
                 "title": "Sözleşme Title",
            }
        }
    )
}
forget_password_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    200: openapi.Response(
        description="A link to reset user password is sent into user's email address",
        examples={
            "application/json": {
                "success": True,
                "message": _("User can reset his/her password via reset link sent into his/her email address.")
            }
        }
    ),
}
forget_password_done_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    200: openapi.Response(
        description="User's email reset done",
        examples={
            "application/json": {
                "success": True,
                "message": _("User's password has changed.")
            }
        }
    ),
}
forget_password_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description="string: user's registered email."),

    })

get_users_to_notify_schema_dict = {
    400: _("Bad Request"),
    201: openapi.Response(
        description="getUsersToNotify",
        examples={
            "application/json": {
                "success": True,
                "message": _("User's email was verified successfully."),
                "user_secret": "cwbz27d43qujz40x4jqeybuoq4vfaj1wwxrcthzk6i*****",
            }
        }
    ),
}
forget_password_done_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        'new_password': openapi.Schema(type=openapi.TYPE_STRING, description="string: user's new_password."),
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description="string: user's encrypted user id."),
        'token': openapi.Schema(type=openapi.TYPE_STRING,
                                description="string: user's one time consumed link for one day"),
    })

vendor_register_step_one_response_schema_dict = {
    400: _("Bad Request"),
    201: openapi.Response(
        description="Email address is verified successfully",
        examples={
            "application/json": [
                {"id": 25, "name": "Cumanıon Dükkanı"},
                {"id": 38, "name": "Deneme Dükkanı"},
                {"id": 39, "name": "Deneme 19 Haziran"}]

        }
    ),
}

vendor_comments_mine_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Customer Own Comments",
        examples={
            "application/json": {

            }
        }
    ),
}
product_status_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Product Status is updated by superuser",
        examples={
            "application/json": {
                "id": 1,
                "status": "approved"
            }
        }
    ),
}
product_comments_mine_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Customer Own Comments",
        examples={
            "application/json": {

            }
        }
    ),
}

sss_entry_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    200: openapi.Response(
        description="New SSS Entry is added in SSS title",
        examples={
            "application/json": {
                "success": True,
                "message": _("new sss_entry is created successfully successfully."),
            }
        }
    ),
}
vendor_register_step_two_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Vendor registration step two (Email Verification Code)",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor verified its email successfully."),
            }
        }
    ),
}
vendor_register_step_four_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Vendor registration password set",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor-user's addresses are set successfully."),
            }
        }
    ),
}

vendor_register_step_three_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Vendor registration password set",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor-user's password is set successfully."),
            }
        }
    ),
}

approve_disapprove_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Vendor registration password set",
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor-user's password is set successfully."),
            }
        }
    ),
}
vendor_send_invoice_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description=_("Vendor sends invoice to customer for order."),
        examples={
            "application/json": {
                "success": True,
            }
        }
    ),
}
vendor_merchant_key_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description=_("Vendor registration password set"),
        examples={
            "application/json": {
                "success": True,
                "merchantKey": "D9V/MqIRitUzA4dutL+nCBvnWfs=",
            }
        }
    ),
}
vendor_company_info_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description=_("Vendor company info"),
        examples={
            "application/json": {
                "success": True,
                "message": _("vendor company's info is set successfully."),
            }
        }
    ),
}

shop_approve_disapprove_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER,
                             description=_("ID of shop which will be approve or disaprove!"))
    })

category_remove_variant_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'variant': openapi.Schema(type=openapi.TYPE_INTEGER,
                                  description=_("You can send individual id or a list of ids."))
    })
category_remove_spec_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'spec': openapi.Schema(type=openapi.TYPE_INTEGER, description=_("You can send individual id or a list of ids."))
    })
product_galery_remove_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'attachment': openapi.Schema(type=openapi.TYPE_INTEGER,
                                     description=_("You can send indiviual id or a list of ids."))
    })

product_galery_remove_response_schema_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    204: openapi.Response(
        description="Deletion is successful",
        examples={
            "application/json": {"status": "success",
                                 "message": _("Attachments removed from galery.")
                                 }
        }
    )
}

product_favourite_response_schema_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    204: openapi.Response(
        description=_("Product is removed from user favourite list!"),
        examples={
            "application/json": {"status": "success",
                                 "message": _("Product is removed from user favourite list!")}
        }
    ),
    201: openapi.Response(
        description="Product is added into user favourite list.",
        examples={
            "application/json": {
                "id": 6,
                "product": {
                    "id": 17,
                    "vendor": {
                        "id": 5,
                        "status": "STEP-4",
                        "company_type": "Anonim Şirket",
                        "reference_code": None,
                        "trade_name": None,
                        "trade_registration_number": None,
                        "store_name": "Topuz Soft",
                        "tckn": "17501613172",
                        "tax_number": "1750161317",
                        "kep_adresi": "asdasdasdasd",
                        "iban": "TR33BUKB20201555555552",
                        "mersis_number": None,
                        "invoice_type": "E-Arşiv Fatura",
                        "links": "",
                        "finance_name": None,
                        "operation_name": None,
                        "finance_phone": None,
                        "operation_phone": None,
                        "finance_email": None,
                        "operation_email": None,
                        "activation_code": None,
                        "is_active": True,
                        "is_approved": False,
                        "is_completed": False,
                        "is_situation": False,
                        "no_sales": False,
                        "personal_data": False,
                        "agreement": False,
                        "check_agreement": False,
                        "logo": None,
                        "remember_token": None,
                        "tax_administration_id": 1,
                        "shipment_company": 1,
                        "background_image": None,
                        "background_color": "#00EEFF",
                        "background_active": True,
                        "font_color": "#00EEFF",
                        "is_deleted": False,
                        "deleted_at": None,
                        "updated_at": "2022-12-05T12:36:31.156944+03:00",
                        "created_at": "2022-12-02T12:03:31.866733+03:00",
                        "user": 43,
                        "main_category": 2,
                        "vergi_dairesi": 74,
                        "invoice_address": None,
                        "company_address": 21,
                        "shop_address": None,
                        "shippment_address": None,
                        "return_address": None,
                        "deleted_by": None,
                        "created_by": None,
                        "files": [
                            {
                                "id": 2,
                                "status": "pending",
                                "title": "Ruhsat Belgesi",
                                "detail": "Altındağ Belediyesi tarafından verilen işyeri açma ruhsatı.",
                                "is_active": True,
                                "is_deleted": False,
                                "deleted_at": None,
                                "updated_at": "2022-12-05T15:29:56.143194+03:00",
                                "created_at": "2022-12-05T15:29:56.143194+03:00",
                                "vendor": 5,
                                "attachment": {
                                    "id": 294,
                                    "slug": "isyeri-acma-ruhsat",
                                    "thumbnail": "http://65.109.128.137:9000/images/20221205/vendor/thumbnail_2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg' %}",
                                    "original": "http://65.109.128.137:9000/images/20221205/vendor/2022_12_05_12_10_52_işyeri_açma_ruhsatı.jpg' %}"
                                },
                                "deleted_by": None,
                                "created_by": 14
                            }
                        ]
                    },
                    "brand": "Hummer",
                    "model": "Av. Tekin Product-1",
                    "name": "Product-1",
                    "barcode": "12313561215",
                    "description": "Variant",
                    "source": None,
                    "image": {
                        "id": 274,
                        "slug": "akbank",
                        "thumbnail": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png' %}",
                        "original": "http://65.109.128.137:9000/images/20221123/bank/2022_11_23_09_19_50_akbank.png' %}"
                    },
                    "galery": [
                        {
                            "id": 105,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/iq.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/iq.svg"
                        },
                        {
                            "id": 104,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/ir.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/ir.svg"
                        },
                        {
                            "id": 103,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/id.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/id.svg"
                        },
                        {
                            "id": 102,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/in.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/in.svg"
                        },
                        {
                            "id": 100,
                            "slug": None,
                            "thumbnail": "http://65.109.128.137:9000/images/flags/thumbnails/hu.svg",
                            "original": "http://65.109.128.137:9000/images/flags/originals/hu.svg"
                        }
                    ],
                    "is_published": False,
                    "comments": [],
                    "category": "Elektronik",
                    "categories": None,
                    "stock": 20,
                    "stock_code": "stock-code11",
                    "kdv": 0,
                    "delivery_time": "Morning",
                    "specs": [],
                    "is_reviewed": False,
                    "reviewed_by": None,
                    "reviewed_at": None,
                    "variants": [],
                    "parent": None,
                    "avg_rate": 0,
                    "total_comments": 0,
                    "comment_statistics": {},
                    "in_mainpage": False,
                    "status": "pending",
                    "feedbacks": [],
                    "hits": 0,
                    "slug": "product-1",
                    "gross_price": "100.00",
                    "hendeseli_price": "0.00",
                    "net_price": "100.00",
                    "discount": 0,
                    "prices": [
                        {
                            "id": 22,
                            "discount": 100,
                            "hendeseli_price": "100.00",
                            "gross_price": "100.00",
                            "net_price": None,
                            "currency": "TRY",
                            "is_active": True,
                            "is_deleted": False,
                            "created_at": "2022-12-05T17:09:57.581738+03:00",
                            "updated_at": "2022-12-05T17:09:57.581738+03:00",
                            "deleted_at": None,
                            "product": 17,
                            "deleted_by": None,
                            "created_by": None
                        }
                    ]
                },
                "created_by": {
                    "id": 27,
                    "username": "c.topuz@yahoo.com",
                    "email": "c.topuz@yahoo.com",
                    "first_name": "Tekin",
                    "last_name": "TOPUZ",
                    "avatar": None,
                    "phone": None,
                    "role": "customer",
                    "is_email_verified": True,
                    "email_verified_at": "2022-11-30T09:31:29+03:00",
                    "is_mobile_verified": True,
                    "mobile_verified_at": None,
                    "date_joined": "2022-11-30T09:30:55+03:00",
                    "groups": [
                        {
                            "id": 1,
                            "name": "Customer",
                            "permissions": []
                        }
                    ],
                    "user_permissions": []
                },
                "price": None
            }
        }
    )
}

category_add_new_spec_response_schema_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    201: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                "id": 4610,
                "spec": {
                    "id": 21,
                    "type": "variable",
                    "name": "Deneme 5/12/2022",
                    "slug": "deneme-5122022",
                    "values": [
                        {
                            "id": 45,
                            "value": "Variable-1",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 46,
                            "value": "Variable-2",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 47,
                            "value": "Variable-3",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        }
                    ]
                },
                "category": 2
            }
        }
    )
}

category_add_new_variant_response_schema_dict = {
    500: _("Internal Server Error"),
    400: _("Bad Request"),
    201: openapi.Response(
        description="New Spec is created and add to category",
        examples={
            "application/json": {
                "id": 4610,
                "spec": {
                    "id": 21,
                    "type": "variable",
                    "name": "Deneme 5/12/2022",
                    "slug": "deneme-5122022",
                    "values": [
                        {
                            "id": 45,
                            "value": "Variable-1",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 46,
                            "value": "Variable-2",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        },
                        {
                            "id": 47,
                            "value": "Variable-3",
                            "image": None,
                            "spec": {
                                "id": 21,
                                "type": "variable",
                                "name": "Deneme 5/12/2022",
                                "slug": "deneme-5122022"
                            }
                        }
                    ]
                },
                "category": 2
            }
        }
    )
}

vendor_register_response_schema_dict = {
    400: _("Bad Request"),
    201: openapi.Response(
        description=_("Vendor has registered successfully."),
        examples={
            "application/json": {
                "refresh": "eyJhbG.eyJ0b2tlblY2QwZjVmYyIsInVzZXJfaWQiOjE4fQ.LPt_XnLC6KWtNE",
                "access": "eyJhbVCJ9.eyJ0b2tlbl9Dc2LCJpYXQiOjE2NjXNlcl9pZCI6MTh9.K6UPz8V0LTxm3qnI",
            }
        }
    )
}

paymentcard_delete_response_schema_dict = {
    400: _("Bad Request"),
    204: openapi.Response(
        description=_("Customer has deleted his/her card from Iyzico successfully."),
        examples={
            "application/json": {
                "success": True,
                "message": _("Customer has deleted his/her card from Iyzico successfully.")
            }
        }
    )
}

password_change_response_schema_dict = {
    400: _("Bad Request"),
    201: openapi.Response(
        description="User password is changed successfully",
        examples={
            "application/json": {
                "refresh": "eyJhbG.eyJ0b2tlblY2QwZjVmYyIsInVzZXJfaWQiOjE4fQ.LPt_XnLC6KWtNE",
                "access": "eyJhbVCJ9.eyJ0b2tlbl9Dc2LCJpYXQiOjE2NjXNlcl9pZCI6MTh9.K6UPz8V0LTxm3qnI",
            }
        }
    )
}

token_response_schema_dict = {
    400: _("Bad Request"),
    201: openapi.Response(
        description="New JWT (JSON Web Token) is created successfully",
        examples={
            "application/json": {
                "refresh": "eyJhbG.eyJ0b2tlblY2QwZjVmYyIsInVzZXJfaWQiOjE4fQ.LPt_XnLC6KWtNE",
                "access": "eyJhbVCJ9.eyJ0b2tlbl9Dc2LCJpYXQiOjE2NjXNlcl9pZCI6MTh9.K6UPz8V0LTxm3qnI",
            }
        }
    )
}

register_response_schema_dict = {
    400: _("Bad Request"),
    201: openapi.Response(
        description="New User is created "
                    "successfully",
        examples={
            "application/json": {
                "access": "JWT TOKEN",
                "refresh": "Refresh TOKEN",
            }
        }
    ),
}

verification_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'token': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    })

verification_response_schema_dict = {
    400: _("Bad Request"),
    200: openapi.Response(
        description="Email address is verified successfully",
        examples={
            "application/json": {
                "success": True,
                "message": _("User's email was verified successfully.")
            }
        }
    ),
}

upload_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        'type': openapi.Schema(type=openapi.TYPE_STRING, description='string: type of action eg. category, avatar'),
        'key': openapi.Schema(type=openapi.TYPE_ARRAY, items={"type": "string", "enum": ["avatar",
                                                                                         "toplu ürün girişi",
                                                                                         "products",
                                                                                         "vendors",
                                                                                         ]},
                              description='array'),
        'file': openapi.Schema(type=openapi.TYPE_FILE, description='file'),
    })

change_password_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string: new password'),
        're_password': openapi.Schema(type=openapi.TYPE_STRING, description='string: new password again'),
        'old_password': openapi.Schema(type=openapi.TYPE_STRING, description='string: user old password'),
    })
order_create_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="New order is created",
        examples={
            "application/json": {
                "success": True,
                "message": _("User has bought everthing in his/her basket successfully.")
            }
        }
    ),
}
my_orders_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="New order is created",
        examples={
            "application/json": {
                "success": True,
                "message": _("User has bought everthing in his/her basket successfully.")
            }
        }
    ),
}


authtoken_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        "token":  openapi.Schema(type=openapi.TYPE_STRING, description='string: token')
    }
)
authtoken_response_body = {
    400: _('There is no iyzico_payment transaction with this order.'),
    500: _(_("Internal Server Error")),
    200: _('Login is SUCCESSFULL.')
}


refund_purchase_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        "basket_products": openapi.Schema(type=openapi.TYPE_ARRAY, items={"type": "int", })}
)

cancel_purchase_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        "order_id": openapi.Schema(type=openapi.TYPE_NUMBER, description='int:order_id'),
        "basket_products": openapi.Schema(type=openapi.TYPE_ARRAY,
                                          items={"type": "object",
                                                 "example": openapi.Schema(
                                                     type=openapi.TYPE_OBJECT,
                                                     content="application/json",
                                                     properties={
                                                         "id": openapi.Schema(type=openapi.TYPE_NUMBER,
                                                                              description='int: basket_product id'),
                                                         "amount": openapi.Schema(type=openapi.TYPE_NUMBER,
                                                                                  description='int: basket_product amount'),
                                                     })
                                                 })}
)

cancel_purchase_response_body = {
    400: _('There is no iyzico_payment transaction with this order.'),
    500: _(_("Internal Server Error")),
    200: _('IYZICO purchase cancellation is SUCCESSFULL.')
}

order_create_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    content="application/json",
    properties={
        "is_3D": openapi.Schema(type=openapi.TYPE_BOOLEAN, description='boolean: Does The User want to pay with 3D?'),
        "paymentCard": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='boolean: User want to pay with 3D',
            properties={
                "cardholdername": openapi.Schema(type=openapi.TYPE_STRING, description='string: cardholdername'),
                "cardNumber": openapi.Schema(type=openapi.TYPE_STRING, description='string: cardNumber'),
                "expireMonth": openapi.Schema(type=openapi.TYPE_STRING, description='string: expireMonth'),
                "expireYear": openapi.Schema(type=openapi.TYPE_STRING, description='string: expireYear'),
                "cvc": openapi.Schema(type=openapi.TYPE_STRING, description='string: cvc'),
                "registerCard": openapi.Schema(type=openapi.TYPE_STRING, description='string: registerCard')
            }),
        "shippingAddress": openapi.Schema(type=openapi.TYPE_NUMBER, description='int: shippingAddress ID'),
        "billingAddress": openapi.Schema(type=openapi.TYPE_NUMBER, description='int: billingAddress ID'),
    })

upload_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 262,
                    "thumbnail": None,
                    "original": "https://cdn.hendeseli.com/images/20221118/2022_11_18_09_16_45_xxxx.png' %}"
                }
            ]
        }
    ),
}
tax_post_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 1,
                    "country": None,
                    "state": None,
                    "zip": None,
                    "city": None,
                    "rate": 2,
                    "name": "Global",
                    "is_global": True,
                    "priority": None,
                    "on_shipping": True,
                    "created_at": "2021-03-25T13:26:57.000Z",
                    "updated_at": "2021-03-25T16:07:18.000Z"
                }
            ]
        }
    ),
}
shop_post_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 1,
                    "owner_id": 1,
                    "name": "Furniture Shop",
                    "slug": "furniture-shop",
                    "description": "The furniture shop is the best shop around the city. This is being run under the store owner and our aim is to provide quality product and hassle free customer service.",
                    "cover_image": {
                        "id": "885",
                        "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/883/Untitled-6.jpg' %}",
                        "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/883/conversions/Untitled-6-thumbnail.jpg' %}"
                    },
                    "logo": {
                        "id": "884",
                        "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/882/Furniture.png' %}",
                        "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/882/conversions/Furniture-thumbnail.jpg' %}"
                    },
                    "is_active": 1,
                    "address": {
                        "zip": "08753",
                        "city": "East Dover",
                        "state": "New Jersey",
                        "country": "USA",
                        "street_address": "588  Finwood Road"
                    },
                    "settings": {
                        "contact": "21342121221",
                        "socials": [
                            {
                                "url": "https://www.instagram.com/",
                                "icon": "InstagramIcon"
                            }
                        ],
                        "website": "https://redq.io/",
                        "location": {
                            "lat": 40.757272,
                            "lng": -74.089508,
                            "city": "Kearny",
                            "state": "NJ",
                            "country": "United States",
                            "formattedAddress": "New Jersey Turnpike, Kearny, NJ, USA"
                        }
                    },
                    "created_at": "2021-06-27T03:46:14.000Z",
                    "updated_at": "2021-07-08T09:27:14.000Z",
                    "orders_count": 8,
                    "products_count": 55,
                    "owner": {
                        "id": 1,
                        "name": "Store Owner",
                        "email": "store_owner@demo.com",
                        "email_verified_at": None,
                        "created_at": "2021-06-27T04:13:00.000000Z",
                        "updated_at": "2021-06-27T04:13:00.000000Z",
                        "is_active": 1,
                        "shop_id": None,
                        "profile": {
                            "id": 1,
                            "avatar": {
                                "id": "883",
                                "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/881/aatik-tasneem-7omHUGhhmZ0-unsplash%402x.png' %}",
                                "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/881/conversions/aatik-tasneem-7omHUGhhmZ0-unsplash%402x-thumbnail.jpg' %}"
                            },
                            "bio": "This is the store owner and we have 6 shops under our banner. We are running all the shops to give our customers hassle-free service and quality products. Our goal is to provide best possible customer service and products for our clients",
                            "socials": None,
                            "contact": "12365141641631",
                            "customer_id": 1,
                            "created_at": "2021-06-30T11:20:29.000000Z",
                            "updated_at": "2021-06-30T14:13:53.000000Z"
                        }
                    }
                },

            ]
        }
    ),
}
tags_post_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 1,
                    "name": "FIrst Edition",
                    "slug": "first-edition",
                    "language": "en",
                    "icon": None,
                    "image": [],
                    "details": None,
                    "type_id": 8,
                    "created_at": "2021-12-08T13:40:17.000Z",
                    "updated_at": "2021-12-08T13:40:17.000Z",
                    "deleted_at": None,
                    "translated_languages": [
                        "en"
                    ],
                    "type": {
                        "id": 8,
                        "name": "Books",
                        "settings": {
                            "isHome": False,
                            "layoutType": "compact",
                            "productCard": "radon"
                        },
                        "slug": "books",
                        "language": "en",
                        "icon": "BookIcon",
                        "promotional_sliders": [],
                        "created_at": "2021-12-07T16:30:18.000000Z",
                        "updated_at": "2021-12-08T13:06:56.000000Z",
                        "translated_languages": [
                            "en"
                        ]
                    }
                },
            ]
        }
    ),
}
category_post_response_schema_dict = {
    400: _("Bad Request"),
    500: _("Internal Server Error"),
    201: openapi.Response(
        description="File upload is successfull",
        examples={
            "application/json": [
                {
                    "id": 1,
                    "name": "Fruits & Vegetables",
                    "slug": "fruits-vegetables",
                    "icon": "FruitsVegetable",
                    "image": [],
                    "details": None,
                    "language": "en",
                    "translated_languages": [
                        "en"
                    ],
                    "parent": None,
                    "type_id": 1,
                    "created_at": "2021-03-08T07:21:31.000Z",
                    "updated_at": "2021-03-08T07:21:31.000Z",
                    "deleted_at": None,
                    "parent_id": None,
                    "type": {
                        "id": 1,
                        "name": "Grocery",
                        "language": "en",
                        "translated_languages": [
                            "en"
                        ],
                        "settings": {
                            "isHome": True,
                            "layoutType": "classic",
                            "productCard": "neon"
                        },
                        "slug": "grocery",
                        "icon": "FruitsVegetable",
                        "promotional_sliders": [
                            {
                                "id": "902",
                                "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/902/offer-5.png' %}",
                                "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/902/conversions/offer-5-thumbnail.jpg' %}"
                            },
                            {
                                "id": "903",
                                "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/903/offer-4.png' %}",
                                "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/903/conversions/offer-4-thumbnail.jpg' %}"
                            },
                            {
                                "id": "904",
                                "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/904/offer-3.png' %}",
                                "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/904/conversions/offer-3-thumbnail.jpg' %}"
                            },
                            {
                                "id": "905",
                                "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/905/offer-2.png' %}",
                                "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/905/conversions/offer-2-thumbnail.jpg' %}"
                            },
                            {
                                "id": "906",
                                "original": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/906/offer-1.png' %}",
                                "thumbnail": "https://pickbazarlaravel.s3.ap-southeast-1.amazonaws.com/906/conversions/offer-1-thumbnail.jpg' %}"
                            }
                        ],
                        "created_at": "2021-03-08T07:18:25.000000Z",
                        "updated_at": "2021-09-26T15:23:32.000000Z"
                    },
                    "children": [
                        {
                            "id": 2,
                            "name": "Fruits",
                            "slug": "fruits",
                            "icon": None,
                            "image": [],
                            "details": None,
                            "language": "en",
                            "translated_languages": [
                                "en"
                            ],
                            "parent": {
                                "id": 1,
                                "name": "Fruits & Vegetables",
                                "slug": "fruits-vegetables",
                                "icon": "FruitsVegetable",
                                "image": [],
                                "details": None,
                                "language": "en",
                                "translated_languages": [
                                    "en"
                                ],
                                "parent": None,
                                "type_id": 1,
                                "created_at": "2021-03-08T07:21:31.000000Z",
                                "updated_at": "2021-03-08T07:21:31.000000Z",
                                "deleted_at": None,
                                "parent_id": None,
                                "type": None,
                                "children": None
                            },
                            "type_id": 1,
                            "created_at": "2021-03-08T07:22:04.000000Z",
                            "updated_at": "2021-03-08T07:22:04.000000Z",
                            "deleted_at": None,
                            "products_count": 9,
                            "parent_id": 1,
                            "children": []
                        },
                        {
                            "id": 3,
                            "name": "Vegetables",
                            "slug": "vegetables",
                            "icon": None,
                            "image": {
                                "id": None,
                                "original": None,
                                "thumbnail": None
                            },
                            "details": None,
                            "language": "en",
                            "translated_languages": [
                                "en"
                            ],
                            "parent": {
                                "id": 1,
                                "name": "Fruits & Vegetables",
                                "slug": "fruits-vegetables",
                                "icon": "FruitsVegetable",
                                "image": [],
                                "details": None,
                                "language": "en",
                                "translated_languages": [
                                    "en"
                                ],
                                "parent": None,
                                "type_id": 1,
                                "created_at": "2021-03-08T07:21:31.000000Z",
                                "updated_at": "2021-03-08T07:21:31.000000Z",
                                "deleted_at": None,
                                "parent_id": None,
                                "type": None,
                                "children": None
                            },
                            "type_id": 1,
                            "created_at": "2021-03-08T07:57:48.000000Z",
                            "updated_at": "2021-03-09T11:51:24.000000Z",
                            "deleted_at": None,
                            "products_count": 11,
                            "parent_id": 1,
                            "children": []
                        }
                    ]
                }
            ]
        }
    ),
}
