import json

true = 'true'
false = 'false'
null =''
jsonData = {
  "openapi": "3.0.0",
  "servers": [
    {
      "description": "SwaggerHub API Auto Mocking",
      "url": "https://virtserver.swaggerhub.com/telkomdds/MyTDSInternalAM/1.0.0"
    }
  ],
  "info": {
    "description": "Mockup API MyTDS Internal AM Update",
    "version": "1.0.0",
    "title": "Telkom Digital Solution AM Update",
    "contact": {
      "email": "telkomdigitalsolution2019@gmail.com"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    }
  },
  "tags": [
    {
      "name": "user",
      "description": "Related to the user of My TDS AM app"
    },
    {
      "name": "ticket",
      "description": "Related to ticket services"
    },
    {
      "name": "order",
      "description": "Related to data order services"
    },
    {
      "name": "notification",
      "description": "Related to all notifications"
    },
    {
      "name": "user management",
      "description": "Related to user management"
    }
  ],
  "paths": {
    "/api/v1/errorResponses500": {
      "get": {
        "tags": [
          "tes"
        ],
        "summary": "error response 500",
        "description": "error response 500",
        "responses": {
          "500": {
            "description": "Bad Request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok500Internal"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v1/integration": {
      "post": {
        "tags": [
          "user"
        ],
        "summary": "update User",
        "requestBody": {
          "description": "update User",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyUpdateUser"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/updateUser200"
                }
              }
            }
          },
          "400": {
            "description": "Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/bulkWrite400"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v1/am-login": {
      "post": {
        "tags": [
          "user"
        ],
        "summary": "login",
        "parameters": [
          {
            "in": "header",
            "name": "applicationType",
            "description": "input web/ app",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "description": "user login to the app",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyLogin"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/login"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok400Login"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok401Login"
                }
              }
            }
          },
          "409": {
            "description": "Bad Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/409LoginResponse"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok500Login"
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/auth/generatetoken": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "generate token",
        "requestBody": {
          "description": "generate token",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/generateToken"
              },
              "example": {
                "clientId": 1,
                "clientSecret": "user01"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/generateToken200"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Your Request Has Been Processed",
                  "data": {
                    "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI5N2IzMzE5My00M2ZmLTRlNTgtOTEyNC1iM2E5YjlmNzJjMzQiLCJleHAiOjE2MTQ5MTY1NzYsImlhdCI6MTYxNDkxNDc3NiwiaXNzIjoidGVsa29tZGV2IiwianRpIjoiNjNjZWUzMTgtNDBkMy00MmNlLTg0YjctOWE1ZDFiZDJkNjU3Iiwic3ViIjoiZEdWc2EyOXRaR2xuYVhSaGJITnZiSFYwYVc5dVpETjIifQ."
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/am-login": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "login",
        "parameters": [
          {
            "in": "header",
            "name": "applicationType",
            "description": "input web/ app",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "requestBody": {
          "description": "user login to the app",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyLogin"
              },
              "example": {
                "username": 123456,
                "password": "mytens2020"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/login"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Your Request Has Been Processed",
                  "data": {
                    "accessToken": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI5N2IzMzE5My00M2ZmLTRlNTgtOTEyNC1iM2E5YjlmNzJjMzQiLCJlbWFpbCI6IjQwMjc4OUB0ZWxrb20uY28uaWQiLCJleHAiOjE2MTQ5MTc3NzEsImlhdCI6MTYxNDkxNTk3MSwiaXNzIjoidGVsa29tZGV2IiwianRpIjoiODgwMjBiNDItY2M5Yy00ZmU1LTk2NzYtNjQ2OTA4MWVkOTVlIiwibmlrIjoiNDAyNzg5IiwicmVmcmVzaCI6IjFlMmIzMWMwLWU1YWQtNDRlNC05YmUxLTA5OGNmNjlmOTdjMCIsInJvbGVVc2VyIjoiYWNjb3VudF9tYW5hZ2VyIiwic3ViIjoiNGJiOGE4ODEtY2YyYy00MTNmLThmM2UtODNiYjBmZjM5MjI4In0",
                    "resfreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI5N2IzMzE5My00M2ZmLTRlNTgtOTEyNC1iM2E5YjlmNzJjMzQiLCJleHAiOjE2MTc1MDc5NzEsImlhdCI6MTY",
                    "accessTokenExpiresIn": 1800,
                    "refreshTokenExpiresIn": 2592000,
                    "subscribe": [
                      "tds_am_develop_5590328",
                      "tds_am_develop_2000472",
                      "tds_am_develop_2920223",
                      "tds_am_develop_5556830",
                      "tds_am_develop_2915060",
                      "tds_am_develop_2910586",
                      "tds_am_develop_2914111",
                      "tds_am_develop_4600145",
                      "tds_am_develop_2000533",
                      "tds_am_develop_10000",
                      "tds_am_catalog_develop_",
                      "tds_marketing_develop_"
                    ],
                    "role": {
                      "roleId": "account_manager",
                      "roleName": "Account Manager",
                      "roleChilds": [

                      ],
                      "apps": [
                        {
                          "appId": "assurance",
                          "appName": "Assurance"
                        },
                        {
                          "appId": "complex",
                          "appName": "Complex"
                        },
                        {
                          "appId": "buying",
                          "appName": "Buying"
                        },
                        {
                          "appId": "catalog",
                          "appName": "Catalog"
                        },
                        {
                          "appId": "delivery",
                          "appName": "Delivery"
                        },
                        {
                          "appId": "partnership",
                          "appName": "Partnership"
                        }
                      ]
                    },
                    "photo": "https://minio-partner-dev.telkomdigitalsolution.co/tdspartner/image/102bc6f4-0713-4dd8-ac41-48a7b8fa683b.png",
                    "fullName": "John Mayer",
                    "sub": "4bb8a881-cf2c-413f",
                    "companyId": "",
                    "ratingDate": "2020-04-17T10:15:14.902Z",
                    "segment": "BMS-2",
                    "bud": "DES",
                    "direktorat": "",
                    "divisi": "",
                    "unit": "",
                    "privileges": [
                      {
                        "category": "Assurance",
                        "feature": [
                          {
                            "name": "link",
                            "function": [
                              "read_list_request",
                              "read_list_active",
                              "read_detail",
                              "update_approveAM",
                              "update_sendParameter",
                              "update_complete"
                            ]
                          }
                        ]
                      }
                    ]
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok400Login"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok401Login"
                }
              }
            }
          },
          "409": {
            "description": "Bad Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/409LoginResponse"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok500Login"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v1/logout-am": {
      "put": {
        "tags": [
          "user"
        ],
        "summary": "logout",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Logout"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/user/am-customer-account": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "list of AM's Customer Account",
        "description": "get the list of AM's Customer Account",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/listCA"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/users/user/v1/am-nipnas/{nik}": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "List of ccHandled's AM",
        "description": "List of ccHandled's AM for Ticket",
        "parameters": [
          {
            "in": "path",
            "name": "nik",
            "required": true,
            "description": "input nik",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListNipnasAM"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get data",
                  "data": [
                    {
                      "nipnas": 3705763,
                      "corporateClientName": "BANK RAKYAT INDONESIA (PERSERO)",
                      "custAccntNum": null,
                      "segment": "BMS-1",
                      "location": "JAKARTA PUSAT",
                      "witel": "JAKARTA SELATAN",
                      "divre": 2,
                      "startHandled": 20191101,
                      "endHandled": 20191130,
                      "ccRemote": "MAIN"
                    },
                    {
                      "nipnas": 3705763,
                      "corporateClientName": "BANK RAKYAT INDONESIA (PERSERO)",
                      "custAccntNum": null,
                      "segment": "BMS-1",
                      "location": "JAKARTA PUSAT",
                      "witel": "JAKARTA SELATAN",
                      "divre": 2,
                      "startHandled": 20191101,
                      "endHandled": 20191130,
                      "ccRemote": "MAIN"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK1"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v2/am-nipnas/{nik}": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "List of ccHandled's AM",
        "description": "List of ccHandled's AM for Squad Delivery",
        "parameters": [
          {
            "in": "path",
            "name": "nik",
            "required": true,
            "description": "input nik",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "message": {
                      "type": "string"
                    },
                    "code": {
                      "type": "integer"
                    },
                    "data": {
                      "$ref": "#/components/schemas/dataNipnas"
                    }
                  }
                },
                "example": {
                  "success": true,
                  "message": "Success get detail contract",
                  "code": 200,
                  "data": [
                    {
                      "nipnas": 4600005,
                      "corporateClientName": "PT. WIRA ARTA TELEMATIKA",
                      "serviceCount": 0,
                      "servicePoint": 0
                    },
                    {
                      "nipnas": 3705763,
                      "corporateClientName": "BANK RAKYAT INDONESIA (PERSERO)",
                      "serviceCount": 4081,
                      "servicePoint": 2989
                    },
                    {
                      "nipnas": 10000,
                      "corporateClientName": "TELEKOMUNIKASI INDONESIA",
                      "serviceCount": 22,
                      "servicePoint": 1
                    },
                    {
                      "nipnas": 2920223,
                      "corporateClientName": "BANK PERMATA (BANK BALI)",
                      "serviceCount": 353,
                      "servicePoint": 302
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK1"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/user/list-ca-am/{nik}": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "list of CA per AM",
        "description": "get CA per AM",
        "parameters": [
          {
            "in": "path",
            "name": "nik",
            "required": true,
            "description": "input nik",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/listCAAM"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK4"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users/user/profile-am-eos": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "profile AM/EOS",
        "description": "get profile AM/EOS",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Profile"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK4"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "404": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/nok404"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v2/faq-login": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "get FAQ from login page",
        "description": "get FAQ from login page",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/faqLogin200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK4"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v2/issue-category": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "function for get issue-category",
        "description": "function for get issue-category",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/issueCategory200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK4"
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v1/engineer-on-site/": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "Get Call EOS",
        "description": "for calling EOS",
        "parameters": [
          {
            "in": "query",
            "name": "tdsTicketId",
            "required": true,
            "description": "input tds ticket id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/callEOS"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK4"
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users/user/v1/rating": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "get rating feedback from user",
        "description": "get rating feedback from user",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/feedback200user"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      },
      "post": {
        "tags": [
          "user"
        ],
        "summary": "function submit rating feedback from user",
        "description": "function submit rating feedback from user",
        "requestBody": {
          "description": "user login to the app",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyRating"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/feedback200body"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/users/user/v2/helpdesk": {
      "get": {
        "tags": [
          "user"
        ],
        "summary": "get contact for helpdesk",
        "description": "get contact for helpdesk",
        "parameters": [
          {
            "in": "query",
            "name": "type",
            "description": "input type contact ex. wa/telephone/chataja",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/helpdesk200contact"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/users-management/v2/profile": {
      "put": {
        "tags": [
          "user management"
        ],
        "summary": "update profile",
        "description": "update profile",
        "requestBody": {
          "description": "update profile",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/profileBody"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/profile201update"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Image can't be processed",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "user management"
        ],
        "summary": "get profile",
        "description": "get profile",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/profile200get"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "User ditemukan",
                  "data": {
                    "_id": "5f6b11c45ba88e2c05be6a1c",
                    "nik": "nikeosdes",
                    "userId": "84fedd67-78c9-43a6-9fb2-f14c7c3238472323",
                    "email": "nikeosdestest@gmail.com",
                    "password": "SjQ5Y+ejCu74ojZzDsCDJd7XDnYNCHWIzC9VrTziOHI=",
                    "salt": "qaO6+vGUF7g=",
                    "applicationType": [
                      "app"
                    ],
                    "createdAt": "2020-05-20T06:03:58.762Z",
                    "updatedAt": "2020-10-15T09:14:41.685Z",
                    "createdBy": "",
                    "updatedBy": "",
                    "needApproval": false,
                    "isActive": true,
                    "metaData": {
                      "nik": "nikeosdes",
                      "email": "nikeosdestest@gmail.com",
                      "fullName": "NIK EOS DUMMY",
                      "location": "Bandung",
                      "phoneNumber": "081350672619",
                      "company": {
                        "id": null,
                        "name": null,
                        "category": null,
                        "subCategory": null
                      },
                      "ccHandled": [
                        {
                          "nipnas": 2912548,
                          "corporateClientName": "ASTRA SEDAYA FINANCE PT",
                          "segment": "FMS",
                          "location": null,
                          "witel": null,
                          "divre": null,
                          "startHandled": null,
                          "endHandled": null,
                          "ccRemote": "MAIN",
                          "custAccntNum": null
                        },
                        {
                          "nipnas": 2912802,
                          "corporateClientName": "FINANSIA MULTI FINANCE",
                          "segment": "FMS",
                          "location": null,
                          "witel": null,
                          "divre": null,
                          "startHandled": null,
                          "endHandled": null,
                          "ccRemote": "REMOTE",
                          "custAccntNum": null
                        }
                      ],
                      "divisionCode": null,
                      "division": null,
                      "unit": null,
                      "subUnit": null,
                      "jobTitle": null,
                      "photo": null,
                      "nipnas": null,
                      "role": {
                        "roleId": "engineer_on_site",
                        "roleName": "Engineer On Site",
                        "roleChilds": [

                        ],
                        "apps": [
                          {
                            "appId": "assurance",
                            "appName": "assurance"
                          },
                          {
                            "appId": "delivery",
                            "appName": "delivery"
                          }
                        ]
                      },
                      "segment": "DES",
                      "customerAccountNumber": null,
                      "firebaseToken": null,
                      "statusInvitation": null,
                      "atasan": {
                        "nik": null,
                        "nama": null,
                        "posisi": null,
                        "objidposisi": null
                      },
                      "nikAm": null,
                      "ratingDate": "2020-07-25T14:24:45.413Z",
                      "ratingStatus": false,
                      "lastLogin": [
                        "2020-10-15T15:15:24.949Z",
                        "2020-10-15T16:11:08.315Z",
                        "2020-10-16T14:53:38.866Z",
                        "2020-10-20T15:37:39.429Z"
                      ],
                      "busUnitDept": "DES",
                      "lastRefreshToken": "2020-10-20T08:50:39.814Z",
                      "nameApp": null,
                      "longUnit": null
                    }
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/profile-photo": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "upload photo",
        "description": "function upload photo (no otp)",
        "requestBody": {
          "description": "body upload photo",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyPhoto"
              },
              "example": {
                "photo": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/profile-picture-for-social-network.png"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/photo200post"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success",
                  "data": {
                    "photo": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/profile-picture-for-social-network.png"
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Image can't be processed",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/otp": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "send OTP code",
        "description": "send OTP code",
        "requestBody": {
          "description": "send OTP code",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyOtp"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/otp200post"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/otp-verify": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "verify OTP code",
        "description": "verify OTP code",
        "requestBody": {
          "description": "verify OTP code",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyOtpVerify"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/otp200verify"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/reset-password": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "reset password screen",
        "description": "reset password screen",
        "requestBody": {
          "description": "reset password",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyForgotPass"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/forgot200password"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "user management"
        ],
        "summary": "reset password",
        "description": "reset password",
        "requestBody": {
          "description": "reset password",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyResetPass"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/reset201password"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/change-password": {
      "put": {
        "tags": [
          "user management"
        ],
        "summary": "change password",
        "description": "change password",
        "requestBody": {
          "description": "change password",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyChangePass"
              },
              "example": {
                "password": "123qwe",
                "confirmPass": "123qwe"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/change201password"
                },
                "example": {
                  "success": true,
                  "code": 201,
                  "message": "Success",
                  "data": {
                    "signatureCode": "123nmdenor458"
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/users-management/v2/check-user": {
      "post": {
        "tags": [
          "user management"
        ],
        "summary": "for check user",
        "description": "for check user",
        "requestBody": {
          "description": "for check user, click example nik for change password. password for update profile",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyCheckUser"
              },
              "examples": {
                "NIK": {
                  "value": {
                    "nik": 926015
                  }
                },
                "Password": {
                  "value": {
                    "nik": 926015,
                    "password": "123qwe"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/check200user"
                },
                "examples": {
                  "NIK": {
                    "value": {
                      "success": true,
                      "code": 200,
                      "message": "Success",
                      "data": {
                        "isLdap": false,
                        "signatureCode": "123nmdenor458",
                        "phone": "082326066070"
                      }
                    }
                  },
                  "Password": {
                    "value": {
                      "success": true,
                      "code": 200,
                      "message": "Success",
                      "data": {
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/services/v2/ifrs/filter": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "reminder contract filter",
        "description": "reminder contract filter",
        "parameters": [
          {
            "in": "query",
            "name": "agreeNum",
            "description": "input agreenumber",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ifrsFilter"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get data",
                  "data": {
                    "title": "Produk",
                    "detail": [
                      {
                        "title": "Semua Produk"
                      },
                      {
                        "title": "ASTINet"
                      },
                      {
                        "title": "VPN IP"
                      }
                    ]
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/services/v1/services-am/{nipnas}": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "get all list data customer by nipnas",
        "description": "get all list data order in data customer by nipnas",
        "parameters": [
          {
            "in": "path",
            "name": "nipnas",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "type",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/listOrderNipnas"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/api/v1/order/services/<custAccntNum>/am": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "list of AM order",
        "description": "get the list of AM order while creating ticket",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListAMOrder"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/api/order/services/symptom/<serviceCategory>/am/v1": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "service's symptoms",
        "description": "get the service's symptoms category",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Symptoms"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/api/order/services-product/INTERNET/v1": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "get services",
        "description": "get services",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Services"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/order/services-symptom/INTERNET/v1": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "get symptom",
        "description": "get symptom",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Symptom"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/order/services/v1/{nipnas}/search": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "suggest SID",
        "description": "get SID suggestions",
        "parameters": [
          {
            "in": "path",
            "name": "nipnas",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "type",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SuggestSID"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/services/v3/services-detail/{sid}": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "detail SID",
        "description": "get detail SID",
        "parameters": [
          {
            "in": "path",
            "name": "sid",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "type",
            "schema": {
              "type": "string"
            },
            "description": "fault_ticket, monitoring_ticket, integration_ticket",
            "example": "monitoring_ticket"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DetailSID"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/services/v3/{nipnas}/search": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "search SID",
        "description": "search SID",
        "parameters": [
          {
            "in": "path",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas company",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "type",
            "required": true,
            "description": "connectivity/non-connectivity",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "sid",
            "required": true,
            "description": "input sid",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SearchSID"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/services/v3/sa-list": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "function for get row id service list",
        "description": "function for get row id service list",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/salist200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/services/v3/service-list": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "function for get all data service list",
        "description": "function for get all data service list",
        "parameters": [
          {
            "in": "query",
            "name": "rowId",
            "required": true,
            "description": "input rowId",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/serviceList200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/api/v1/ticket": {
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "create ticket",
        "requestBody": {
          "description": "create ticket",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FormCreateTicketConn"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateTicket"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/categories": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "List categories tickets",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/categoriesTickets200"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/dashboard/count-ticket": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "OSM can view dashboard performance of tickets",
        "parameters": [
          {
            "in": "query",
            "name": "dateTime",
            "description": "input dateTime by monthYear ex. 012020",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/dashboardTicket200"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/mytds": {
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "create ticket for EOS",
        "requestBody": {
          "description": "create ticket for EOS (add attach image)",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/eosCreateTicket"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateTicket"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/ticket-am-nonconn": {
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "create ticket non-connectivity",
        "requestBody": {
          "description": "create ticket non-connectivity",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/FormCreateTicketNonConn"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateTicketNonConn"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/worklog": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get list ticket for worklog",
        "description": "get list ticket for worklog in chat feature",
        "parameters": [
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/worklog200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "post ticket for worklog",
        "description": "post ticket for worklog in chat feature",
        "requestBody": {
          "description": "body worklog",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyAddWorklog"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/200AddWorklog"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/worklog-detail/{ticketId}": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get detail ticket for worklog",
        "description": "get detail ticket for worklog in chat feature",
        "parameters": [
          {
            "in": "path",
            "name": "ticketId",
            "required": true,
            "description": "input ticketId",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/worklogDetail200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/chat/count": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get count chat worklog",
        "description": "get count chat worklog",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/countWorklog"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/am": {
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "create ticket am",
        "description": "create ticket am",
        "requestBody": {
          "description": "create ticket",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createTicketAM"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/200TicketAM"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get list ticket",
        "description": "get list ticket by CA",
        "parameters": [
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "status",
            "required": true,
            "description": "input status by active ticket or history ticket",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListTicket"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/am/cc/{nipnas}": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get list ticket by nipnas",
        "description": "get list ticket by NIPNAS with status filter",
        "parameters": [
          {
            "in": "path",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "status",
            "required": true,
            "description": "input status",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "channel",
            "description": "input channel from",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListTicket"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/worklog/{worklogId}/read": {
      "put": {
        "tags": [
          "ticket"
        ],
        "summary": "update isRead",
        "description": "update isRead",
        "parameters": [
          {
            "in": "path",
            "name": "worklogId",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/worklogRead"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/other-channel": {
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "post ticket for other channel",
        "description": "ticket for other channel",
        "requestBody": {
          "description": "ticket for other channel",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ticketOtherChannel"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ticketOtherChannel200"
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/NOK"
                    },
                    {
                      "$ref": "#/components/schemas/nok500Internal"
                    }
                  ]
                }
              }
            }
          }
        }
      },
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get list ticket from other channel",
        "description": "get list ticket from other channel",
        "parameters": [
          {
            "in": "query",
            "name": "corporateClientName",
            "required": true,
            "description": "input company name",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "ticketId",
            "required": true,
            "description": "input ticket id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListTicket"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v2/other-channel": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get list ticket from other channel",
        "description": "get list ticket from other channel",
        "parameters": [
          {
            "in": "query",
            "name": "corporateClientName",
            "required": true,
            "description": "input company name",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input size",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "ticketId",
            "required": true,
            "description": "input ticket id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListTicket"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v2/other-channel/{ticketId}": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get detail ticket from other channel",
        "description": "get detail ticket by ticket ID from other channel",
        "parameters": [
          {
            "in": "path",
            "name": "ticketId",
            "required": true,
            "description": "input ticketId",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/detailTicketEOSAM"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NOK3"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/{ticketId}": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get detail ticket",
        "description": "get detail ticket for AM/ EOS by ticket ID",
        "parameters": [
          {
            "in": "path",
            "name": "ticketId",
            "required": true,
            "description": "input ticketId",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/detailTicketEOSAM"
                },
                "examples": {
                  "Reject": {
                    "value": {
                      "success": true,
                      "code": 200,
                      "message": "Here are the detail for undefined",
                      "data": {
                        "tdsTicketId": "TDS-3001068401-00309614591555051969568",
                        "ticketId": "Gangguan Tervalidasi",
                        "sid": "4709630-1973",
                        "corporateClientName": "TELKOMSEL",
                        "categoryName": "E001",
                        "serviceName": "Astinet 100M",
                        "location": "Jln Cihanjuang, Cimahi, Jawa Barat",
                        "status": [

                        ],
                        "statusTicket": "Reject",
                        "createdAt": "2019-02-06T04:40:55.190Z",
                        "updatedAt": "2019-02-12T10:53:47.669Z",
                        "picName": "John Mayer",
                        "picPhoneNumber": "082326066070",
                        "channel": "MyTDS",
                        "reason": "Tes",
                        "attachment": [
                          {
                            "image": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/profile-picture-for-social-network.png",
                            "fileName": "mytds.png"
                          },
                          {
                            "image": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/profile-picture-for-social-network.png",
                            "fileName": "mytds.png"
                          },
                          {
                            "image": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/profile-picture-for-social-network.png",
                            "fileName": "mytds.png"
                          }
                        ]
                      }
                    }
                  },
                  "Detail Ticket": {
                    "value": {
                      "success": true,
                      "code": 200,
                      "message": "Here are the detail for undefined",
                      "data": {
                        "tdsTicketId": "TDS-3001068401-00309614591555051969568",
                        "ticketId": "IN123459",
                        "sid": "4709630-1973",
                        "ipWan": "-",
                        "corporateClientName": "TELKOMSEL",
                        "categoryName": "E001",
                        "serviceName": "VPN IP 10 Mbps",
                        "location": "Jln Cihanjuang, Cimahi, Jawa Barat",
                        "complaint": "Tidak bisa internetan padahal semua led di STB sudah oke",
                        "status": [
                          {
                            "status": "Tiket Terbit",
                            "dateTime": "2019-02-12T10:31:46.781Z"
                          },
                          {
                            "status": "Penanganan",
                            "dateTime": null,
                            "detail": [
                              {
                                "step": 1,
                                "status": "Send to Tier 2",
                                "statusAlias": "Analisa Teknis",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdby": "NOSSA"
                              },
                              {
                                "step": 2,
                                "status": "NetCool Wait for Impacted Services",
                                "statusAlias": "Analisa Teknis",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              },
                              {
                                "step": 3,
                                "status": "Pending-SLA Hold",
                                "statusAlias": "Penanganan Tertunda",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              },
                              {
                                "step": 4,
                                "status": "Send to Tier 3",
                                "statusAlias": "Penanganan Teknis",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              },
                              {
                                "step": 5,
                                "status": "Final Check",
                                "statusAlias": "Penyelesaian Masalah",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              },
                              {
                                "step": 6,
                                "status": "Resolved (Technical Closed)",
                                "statusAlias": "Penyelesaian Masalah",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              },
                              {
                                "step": 7,
                                "status": "Media Caring",
                                "statusAlias": "Penyelesaian Masalah",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              },
                              {
                                "step": 8,
                                "status": "Salam Simpatik",
                                "statusAlias": "Penyelesaian Masalah",
                                "note": "VPN IP Mati Total Logic",
                                "dateTime": null,
                                "createdBy": ""
                              }
                            ]
                          },
                          {
                            "status": "Closed",
                            "statusAlias": "Selesai",
                            "dateTime": null
                          }
                        ],
                        "statusTicket": "Tiket Terbit",
                        "createdAt": "2019-02-06T04:40:55.190Z",
                        "updatedAt": "2019-02-12T10:53:47.669Z",
                        "picName": "Novi",
                        "picPhoneNumber": "082326066070",
                        "channel": "from MyTDS"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/request/detail": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "get data ticket created by AM",
        "description": "function get ticket in form request ticket",
        "parameters": [
          {
            "in": "query",
            "name": "ticketId",
            "required": true,
            "description": "input tds ticket id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/request200get"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get ticket",
                  "data": {
                    "corporateClientName": "BANK RAKYAT INDONESIA (PERSERO)",
                    "serviceCategory": "Data dan Internet",
                    "sid": "12345TES2",
                    "ipWan": null,
                    "location": "Jln Cihanjuang, Cimahi, Jawa Barat",
                    "serviceName": "Astinet 100M",
                    "defaultSymptom": "Koneksi Putus",
                    "symptoms": [
                      {
                        "symptomId": "A_INTERNET \\\\\\\\ A_INTERNET_001 \\\\\\\\ A_INTERNET_001_001 \\\\\\\\ A_INTERNET_001_001_001",
                        "symptomDescription": "Tidak Bisa Browsing - Tidak Bisa Koneksi"
                      },
                      {
                        "symptomId": "C_CONN \\\\ C_CONN_001 \\\\ C_CONN_001_001 \\\\ C_CONN_001_001_002",
                        "symptomDescription": "Mati Total Logic"
                      },
                      {
                        "symptomId": "C_CONN \\\\ C_CONN_001 \\\\ C_CONN_001_001 \\\\ C_CONN_001_001_002",
                        "symptomDescription": "Intermitten"
                      }
                    ],
                    "complaint": "Nelpon ke KPK tapi nyambung nya ke Vanessa Angel, tolong fix segera ada yang korupsi di kantor kades",
                    "node": "PE-D3-LBG-VPN",
                    "interface": "Gi0/7/0/10.3610",
                    "description": "470089-0029677009 VPN IP KIMIA FARMA Jl Cihampelas No 5 Bandung",
                    "picName": "Arnold",
                    "picPhoneNumber": "0821123456789"
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad input parameter"
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/request/approve": {
      "put": {
        "tags": [
          "ticket"
        ],
        "summary": "approval ticket by eos",
        "description": "approval ticket by eos",
        "requestBody": {
          "description": "approve ticket",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyApprove"
              },
              "example": {
                "ticketId": "TDS-1992",
                "corporateClientName": "BANK RAKYAT INDONESIA (PERSERO)",
                "serviceCategory": "Data dan Internet",
                "sid": "12345TES2",
                "ipWan": null,
                "location": "Jln Cihanjuang, Cimahi, Jawa Barat",
                "serviceName": "Astinet 100M",
                "symptomId": "C_CONN \\\\ C_CONN_001 \\\\ C_CONN_001_001 \\\\ C_CONN_001_001_003",
                "symptomName": "Mati Total",
                "complaint": "Internet mati total nih dari jam 12, kan mau ngegame",
                "node": "PE-D3-LBG-VPN",
                "interfaces": "Gi0/7/0/10.3610",
                "description": "470089-0029677009 VPN IP KIMIA FARMA Jl Cihampelas No 5 Bandung",
                "picName": "Arnold",
                "picPhoneNumber": "0821123456789"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/approve201ticket"
                },
                "example": {
                  "success": true,
                  "code": 201,
                  "message": "Success approve ticket",
                  "data": {
                    "ticketId": "TDS-181206085424101024",
                    "ticketNossa": "IN1995"
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Failed to submit ticket",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/request/reject": {
      "put": {
        "tags": [
          "ticket"
        ],
        "summary": "reject ticket by eos",
        "description": "reject ticket by eos",
        "requestBody": {
          "description": "reject ticket",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyReject"
              },
              "example": {
                "ticketId": "TDS-181206085424101024",
                "reason": "Modem sudah di restart, internet sudah hidup kembali",
                "attachment": [
                  {
                    "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                  },
                  {
                    "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                  },
                  {
                    "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/reject201ticket"
                },
                "example": {
                  "success": true,
                  "code": 201,
                  "message": "Success reject ticket",
                  "data": {
                    "ticketId": "TDS-181206085424101024"
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Failed to reject ticket",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/search": {
      "get": {
        "tags": [
          "ticket"
        ],
        "summary": "function search ticket",
        "description": "function search ticket",
        "parameters": [
          {
            "in": "query",
            "name": "ticketId",
            "description": "input ticket id",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "status",
            "description": "input status worklog ticket",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "description": "input page",
            "required": true,
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "size",
            "description": "input session",
            "required": true,
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "description": "input nipnas",
            "required": true,
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "keyword",
            "description": "input keyword",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/search200ticket"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success filter ticket",
                  "data": [
                    {
                      "ticketId": "TDS-S00011553221093907",
                      "id": "IN00029300021",
                      "category": "E001",
                      "corporateClientName": "PT. Pertamina",
                      "serviceId": "4700167-16502",
                      "serviceName": "Astinet 100M",
                      "location": "Jln Cihanjuang, Cimahi, Jawa Barat",
                      "complaint": "Tidak bisa internetan padahal semua led di STB sudah oke",
                      "status": "Penanganan",
                      "createdAt": "22/03/2019 - 09:18",
                      "channel": "from MyTDS",
                      "rating": {
                        "value": 4,
                        "dateTime": "2019-03-25 01:46:39 UTC",
                        "message": "Terbaik"
                      }
                    }
                  ],
                  "meta": {
                    "page": 1,
                    "size": 10,
                    "totalPage": 1,
                    "totalData": 4
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Failed to reject ticket",
                  "data": {
                  }
                }
              }
            }
          },
          "500": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/500"
                },
                "example": {
                  "success": false,
                  "code": 500,
                  "message": "Internal server error",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/tickets/ticket/v1/upload-file": {
      "post": {
        "tags": [
          "ticket"
        ],
        "summary": "function upload file",
        "requestBody": {
          "description": "body upload file",
          "required": true,
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "properties": {
                  "ticketId": {
                    "type": "string"
                  },
                  "file": {
                    "type": "string",
                    "format": "binary"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/postUploadFile"
                },
                "example": {
                  "success": true,
                  "code": 201,
                  "message": "Success upload file",
                  "data": {
                    "fileName": "mytds.png",
                    "fileUrl": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/profile-picture-for-social-network.png"
                  }
                }
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "ticket"
        ],
        "summary": "delete file",
        "description": "delete file",
        "parameters": [
          {
            "in": "query",
            "name": "ticketId",
            "required": true,
            "description": "input ticket id",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "fileName",
            "required": true,
            "description": "input file name",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/deleteFile"
                },
                "example": {
                  "success": true,
                  "code": 201,
                  "message": "Success delete file",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/slg/v1": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "SLG list in periode/months",
        "description": "get SLG list in periode/months",
        "parameters": [
          {
            "in": "query",
            "name": "startDate",
            "description": "filter date mulai dari tanggal ex. 201901",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "endDate",
            "description": "filter date sampai tanggal ex. 201901",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "description": "nomor nipnas",
            "required": true,
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/slgPeriode"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/slg/v1/{periode}": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "SLG list per periode",
        "description": "get SLG list per periode",
        "parameters": [
          {
            "in": "path",
            "name": "periode",
            "description": "input id label",
            "required": true,
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "page",
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "description": "input size",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListSlgPerPeriode"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/slg/v1/{periode}/download-slg": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "download SLG",
        "description": "download SLG list per periode per nipnas",
        "parameters": [
          {
            "in": "path",
            "name": "periode",
            "description": "input id label",
            "required": true,
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DownloadSlg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/slg/v2/{periode}/{sid}": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "detail SLG versioning 1",
        "description": "get detail SLG versioning 1",
        "parameters": [
          {
            "in": "path",
            "name": "periode",
            "required": true,
            "description": "input label id ex 201812",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "sid",
            "required": true,
            "description": "input sid user",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DetailSlg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/slg/v2/{periodeCode}/slg-detail": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "detail SLG versioning 2",
        "description": "get detail SLG versioning 2",
        "parameters": [
          {
            "in": "path",
            "name": "periodeCode",
            "required": true,
            "description": "input label id ex 201812",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "sid",
            "required": true,
            "description": "input sid user",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DetailSlg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/slg/v1/{periode}/search": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "search SLG",
        "description": "search SLG",
        "parameters": [
          {
            "in": "path",
            "name": "periode",
            "required": true,
            "description": "input label id",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "serviceId",
            "required": true,
            "description": "input serviceId",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SearchSlg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/mrtg/v2/mrtg-am": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "get list MRTG",
        "description": "get list MRTG",
        "parameters": [
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListMrtg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/mrtg/v1/{sid}": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "detail MRTG",
        "description": "get detail MRTG",
        "parameters": [
          {
            "in": "path",
            "name": "sid",
            "required": true,
            "description": "input sid user",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "start",
            "required": true,
            "description": "filter date mulai dari tanggal ex. 2012-12-28",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "end",
            "required": true,
            "description": "filter date sampai tanggal ex. 2012-12-29",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DetailMrtg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/mrtg/v1/search": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "search MRTG",
        "description": "search MRTG",
        "parameters": [
          {
            "in": "query",
            "name": "nipnas",
            "description": "input nipnas",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "serviceId",
            "description": "input serviceId",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/SearchMrtg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/orders/mrtg/v1/mrtg-request": {
      "post": {
        "tags": [
          "order"
        ],
        "summary": "request MRTG",
        "description": "request MRTG",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MrtgRequest"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/api/v1/order/services/{nipnas}": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "list of customer's portofolio",
        "description": "get list of customer's portofolio",
        "parameters": [
          {
            "in": "path",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListPortofolioCustomer"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/orders/slg/v1/{periode}/download-fault": {
      "get": {
        "tags": [
          "order"
        ],
        "summary": "download Fault Report",
        "description": "download Fault Report",
        "parameters": [
          {
            "in": "path",
            "name": "periode",
            "required": true,
            "description": "input periode",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "nipnas",
            "required": true,
            "description": "input nipnas",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DownloadSlg"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          },
          "401": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/401tokenInvalid"
                },
                "example": {
                  "success": false,
                  "code": 401,
                  "message": "Token is not valid!",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/notifications/notification/v1/all": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "notification list",
        "description": "get AM notification list",
        "parameters": [
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "type",
            "required": true,
            "description": "input type notification",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/allNotifResp"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get list notification",
                  "data": [
                    {
                      "notificationId": "180238-123sada23-1283189-asd1299",
                      "date": "2018-10-13T19:00:00.000Z",
                      "type": "request_ticket",
                      "role": "engineer_on_site",
                      "nipnas": 2920223,
                      "channel": "MyTDS",
                      "title": "Pengajuan Tiket Gangguan",
                      "message": "John Mayer (AM) mengajukan tiket gangguan layanan untuk CC PT Pertamina dengan nomor SID 1125113782",
                      "data": {
                        "tdsTicketId": "TDS-3001068401"
                      },
                      "isRead": false
                    },
                    {
                      "notificationId": "86aef84e-72a1-41df-b815-fb4cad5d61e3",
                      "date": "2019-11-06T08:10:18.928Z",
                      "type": "promo",
                      "custAccntNum": 3001068401,
                      "title": "Jaringan Internet Handal Untuk Bisnis Anda",
                      "message": "ASTINet layanan internet 24/7 dengan availability mencapai 99,9%",
                      "data": {
                        "productId": "prod036",
                        "marketableTitle": "ASTINet - Jaringan Internet Handal Untuk Bisnis Anda",
                        "description": "Jika Anda memerlukan layanan akses internet secara dedicated yang dapat digunakan untuk akses internet secara terus-menerus selama 24 jam sehari dan 7 hari dalam seminggu dengan reliabilitas yang handal dan performansi akses yang baik ditunjang dengan ketersediaan bandwidth ke global internet maka produk ASTINet sangat cocok.  Layanan ASTINet ini memiliki spesifikasi rasio upload donwload sebesar 1:1 dan Anda akan mendapatkan satu blok IP Publik yang dapat digunakan untuk server maupun kepentingan lain. Untuk info lebih lanjut, silakan pilih tombol Lihat Info Selengkapnya dibawah.",
                        "date": "2019-11-06T08:10:18.928Z"
                      },
                      "isRead": true
                    },
                    {
                      "notificationId": "8947343bb-6802-4bc5-b13b-985cc6etd280",
                      "date": "2020-09-09T09:01:19.700Z",
                      "type": "document",
                      "nipnas": 3001068401,
                      "title": "Penyediaan layanan telkom solution",
                      "message": "Kontrak Anda akan berakhir dalam 1 Hari lagi dan Anda belum melakukan konfirmasi untuk perpanjangan kontrak dengan detail berikut.",
                      "data": {
                        "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                        "documentType": "ifrs"
                      },
                      "isRead": false
                    },
                    {
                      "notificationId": "8947343bb-6802-4bc5-b13b-985cc6etd280",
                      "date": "2020-09-09T09:01:19.700Z",
                      "type": "general",
                      "nipnas": 3001068401,
                      "title": "Isi Aktivitas",
                      "message": "Supaya tidak lupa, isi yuk semua kegiatan kamu hari ini melalui menu Aktivitas Saya.",
                      "data": {
                        "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                        "documentType": "activity_create_reminder"
                      },
                      "isRead": false
                    },
                    {
                      "notificationId": "538143bb-4443-7od1-b13b-690cc6cbbwn3",
                      "date": "2020-09-09T09:01:19.700Z",
                      "type": "general",
                      "title": "MyTDS Reward Month",
                      "message": "Yuk, tingkatkan aktivitas harianmu di MyTDS GoBeyond, berikan feedback berkualitas yang membuat MyTDS GoBeyond jadi lebih baik, dan menangkan hadiahnya!",
                      "data": {
                        "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                        "documentType": "access"
                      },
                      "isRead": false
                    },
                    {
                      "notificationId": "180238-123sada23-1283189-asd1299",
                      "date": "2018-10-13T19:00:00.000Z",
                      "type": "ticket",
                      "role": "engineer_on_site",
                      "nipnas": 2920223,
                      "channel": "MyCx",
                      "title": "Validasi",
                      "message": "Laporan Gangguan Anda Telah Kami Terima. Mohon tunggu beberapa menit untuk proses validasi",
                      "data": {
                        "tdsTicketId": "TDS-3001068401",
                        "tdsTicketNossa": "",
                        "corporateClientName": "BANK PERMATA (BANK BALI)",
                        "serviceId": 1125113782,
                        "serviceName": "Metro Link",
                        "serviceLocation": "Jl. Kebon Sirih I, DKI Jakarta",
                        "detailText": "LIHAT DETAIL TICKET GANGGUAN"
                      },
                      "isRead": true
                    }
                  ],
                  "meta": {
                    "page": 1,
                    "size": 10,
                    "totalPage": 1,
                    "totalData": 3
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/notifications/notification/v2/ifrs/{ifrsId}": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "detail notification agreement",
        "description": "detail notification agreement",
        "parameters": [
          {
            "in": "path",
            "name": "ifrsId",
            "description": "input ifrs id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "code": {
                      "type": "integer"
                    },
                    "message": {
                      "type": "string"
                    },
                    "data": {
                      "$ref": "#/components/schemas/detailIfrs200"
                    }
                  }
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get detail IFRS",
                  "data": {
                    "agreeName": "Pengadaan IOT pada Bank Mandiri Cabang Surabaya",
                    "agreeNum": "K.TEL./HK.81045656/DES-MCS/2018",
                    "corporateClientName": "PT Angkasa Pura",
                    "startDate": "1 September 2016",
                    "endDate": "31 Agustus 2020",
                    "serviceCount": 3,
                    "contractValue": 0,
                    "file": {
                      "docName": "Prensentasi Oni Channel",
                      "docUrl": "https://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/BASO%20KFC%2023%20LOKASI%201401A.pdf",
                      "fileType": "pdf"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/notifications/notification/v2/list-ifrs/{ifrsId}": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "list notification agreement",
        "description": "list notification agreement",
        "parameters": [
          {
            "in": "path",
            "name": "ifrsId",
            "description": "input ifrs id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "orderStatus",
            "required": false,
            "description": "input order status",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "serviceName",
            "required": false,
            "description": "input service name",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "code": {
                      "type": "integer"
                    },
                    "message": {
                      "type": "string"
                    },
                    "data": {
                      "$ref": "#/components/schemas/detailIfrs200"
                    }
                  }
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get detail IFRS",
                  "data": [
                    {
                      "sid": "4700030-1938",
                      "serviceName": "VPN IP 10 Mbps",
                      "location": "Jl. Kebon Sirih No. 12, RT.11/RW.2, Gambir, Kota Jakarta Pusat",
                      "orderStatus": "SO"
                    },
                    {
                      "sid": "4700030-2902",
                      "serviceName": "Astinet 10 Mbps",
                      "location": "Jl. Kebon Sirih No. 12, RT.11/RW.2, Gambir, Kota Jakarta Pusat",
                      "orderStatus": "MO"
                    },
                    {
                      "sid": "4700030-2912",
                      "serviceName": "Astinet 100 Mbps",
                      "location": "Jl. Kebon Sirih No. 12, RT.11/RW.2, Gambir, Kota Jakarta Pusat",
                      "orderStatus": "MO"
                    }
                  ],
                  "meta": {
                    "page": 1,
                    "size": 10,
                    "totalPage": 1,
                    "totalData": 3
                  }
                }
              }
            }
          },
          "400": {
            "description": "NOK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/400"
                },
                "example": {
                  "success": false,
                  "code": 400,
                  "message": "Bad Request",
                  "data": {
                  }
                }
              }
            }
          }
        }
      }
    },
    "/notifications/notification/v1/am": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "notification list",
        "description": "get AM notification list",
        "parameters": [
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NotifList"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      },
      "post": {
        "tags": [
          "notification"
        ],
        "summary": "ticket & ifrs type notification",
        "requestBody": {
          "description": "/components/schemas/NotifTicket untuk type Ticket || /components/schemas/NotifTicket untuk type Ifrs",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "oneOf": [
                  {
                    "$ref": "#/components/schemas/NotifTicket"
                  },
                  {
                    "$ref": "#/components/schemas/NotifIfrs"
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "oneOf": [
                    {
                      "$ref": "#/components/schemas/200NotifTicket"
                    },
                    {
                      "$ref": "#/components/schemas/200NotifIfrs"
                    }
                  ]
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/notifications/notification/v1/am/count": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "total number/count of notification list",
        "description": "get the total number of AM notification list",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/NotifCount"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/notifications/notification/v1/{notificationId}/read": {
      "put": {
        "tags": [
          "notification"
        ],
        "summary": "function for isRead true or false",
        "description": "function for isRead true or false",
        "parameters": [
          {
            "in": "path",
            "name": "notificationId",
            "required": true,
            "description": "input notification id",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IsRead"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/notifications/notification/v1/read": {
      "put": {
        "tags": [
          "notification"
        ],
        "summary": "function for isRead true or false",
        "description": "function for isRead true or false",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/IsRead"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/notifications/email/v1/helpdesk": {
      "post": {
        "tags": [
          "notification"
        ],
        "summary": "function for input form contact us",
        "description": "function for input form contact us",
        "requestBody": {
          "description": "create ticket connectivity",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyHelpdesk"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/helpdesk200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/notifications/notification/v1/analytic/helpdesk": {
      "post": {
        "tags": [
          "notification"
        ],
        "summary": "function for analytic logstash helpdesk",
        "description": "function for analytic logstash helpdesk",
        "requestBody": {
          "description": "logstash helpdesk",
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/bodyLogstashHelpdesk"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/helpdeskAnalytic200"
                }
              }
            }
          },
          "400": {
            "description": "bad input parameter"
          }
        }
      }
    },
    "/notifications/notification/v2/document": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "detail notification",
        "description": "get detail notification",
        "parameters": [
          {
            "in": "query",
            "name": "notificationId",
            "required": true,
            "description": "input notificationId",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/notif200doc"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get data",
                  "data": {
                    "title": "Tindak Lanjut Dokumen PT Pertamina (Persero) Bulan November 2021",
                    "greeting": "Hi Annisa,\nBerikut terlampir beberapa dokumen yang perlu untuk ditindaklanjuti",
                    "header": "Untuk menghindari layanan tersuspen/isolir mohon segera lakukan konfirmasi kepada pelanggan terkait kontrak yang akan berakhir:",
                    "point": [
                      {
                        "row": "1. Jika pelanggan meminta perpanjang kontrak tanpa ada perubahan segera lakukan perpanjangan kontrak dan input MO Renewal Agreement pada aplikasi NCX"
                      },
                      {
                        "row": "2. Mohon selalu monitor perpanjangan"
                      },
                      {
                        "row": "3. Jika pelanggan atas nama tersebut tidak masuk dalam pengelolaan Anda, mohon dilaporkan kepada Manajer Segmen/BS/BGES agar dapat ditindaklanjuti"
                      }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    },
    "/notifications/notification/v2/list-docs": {
      "get": {
        "tags": [
          "notification"
        ],
        "summary": "list documents",
        "description": "get list documents",
        "parameters": [
          {
            "in": "query",
            "name": "notificationId",
            "required": true,
            "description": "input notificationId",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "documentType",
            "description": "input documentType",
            "example": "ifrs",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "page",
            "required": true,
            "description": "input page",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "size",
            "required": true,
            "description": "input session",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/list200docs"
                },
                "example": {
                  "success": true,
                  "code": 200,
                  "message": "Success get data",
                  "data": [
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "Pengadaan Jaringan Infrastruktur PT Pertamina (Persero)",
                      "agreeNum": "K.TEL/HK.81045656/DES-MCS/2018",
                      "endContract": "30 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "PKS POLDA NEW",
                      "agreeNum": "K.TEL.32/HK.820/R7W-7G460000/2020",
                      "endContract": "28 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5945f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "KFS PT. Indomarco (6 Lokasi)",
                      "agreeNum": "K.TEL.07-323/HK.810/R7W-7A470000/2019",
                      "endContract": "15 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "PKS DISKOMINFO KONSEL 2020 (CPE EOS)",
                      "agreeNum": "K.TEL.91/HK.810/WTL-7100000/2018",
                      "endContract": "20 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "KFS SMAN 1 KARAMBITAN",
                      "agreeNum": "K.Tel.152/HK 810/R5W-5J460000/2019-1",
                      "endContract": "1 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5802g9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "KFS INDOMARCO PERPANJANGAN 1 DES 2018 FINAL (3)",
                      "agreeNum": "K.TEL.3723/HK.810/R3W-3C430000/2019/1-3730218429",
                      "endContract": "1 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "Pengadaan Jaringan Infrastruktur PT Pertamina (Persero)",
                      "agreeNum": "K.TEL.04-0998/HK.810/DES-00/2019_1",
                      "endContract": "3 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-3ec0-9c7b-3e437d0dccae",
                      "agreeName": "PERPANJ PT.BPR UKA BIMA KHATULISTIWA 20180001",
                      "agreeNum": "K.TEL 205/HK.820/WTL-6D10000/2018",
                      "endContract": "8 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0ddcae",
                      "agreeName": "AmdUp PT RENALTEAM HEMODIALISIS PONDOK INDAH Kalibrasi_20200303_0001",
                      "agreeNum": "K.TEL.0276/HK.820/R2W-2D470000/2020",
                      "endContract": "3 Maret 2021",
                      "contractValue": 0
                    },
                    {
                      "id": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                      "agreeName": "0276 2020.03.02.AmdUp PT RENALTEAM HEMODIALISIS PONDOK INDAH Kalibrasi_20200303_0001",
                      "agreeNum": "K.TEL.0276/HK.820/R2W-2D470000/2020",
                      "endContract": "30 Maret 2021",
                      "contractValue": 0
                    }
                  ],
                  "meta": {
                    "page": 1,
                    "size": 10,
                    "totalData": 20,
                    "totalPage": 2
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "bodyLogin": {
        "type": "object",
        "properties": {
          "nik": {
            "type": "string"
          },
          "password": {
            "type": "string"
          }
        }
      },
      "generateToken": {
        "type": "object",
        "properties": {
          "clientId": {
            "type": "string"
          },
          "clientSecret": {
            "type": "string"
          }
        }
      },
      "generateToken200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "accessToken": {
                "type": "string"
              }
            }
          }
        }
      },
      "categoriesTickets200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/categoriesTicketsType"
            },
            "example": [
              {
                "id": "datin",
                "name": "Data dan Internet"
              }
            ]
          }
        }
      },
      "categoriesTicketsType": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "name": {
            "type": "string"
          }
        }
      },
      "dashboardTicket200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "properties": {
              "dateTime": {
                "type": "string",
                "example": "1-31 Januari 2020"
              },
              "totalTicketPublish": {
                "type": "integer",
                "example": 141
              },
              "totalHandlingTicket": {
                "type": "integer",
                "example": 112
              },
              "totalTicketCompleted": {
                "type": "integer",
                "example": 101
              },
              "ticketPublish": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "example": [
                  5,
                  15,
                  10,
                  6,
                  12,
                  8,
                  20,
                  25,
                  13,
                  27
                ]
              },
              "ticketHandling": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "example": [
                  5,
                  10,
                  8,
                  4,
                  9,
                  7,
                  16,
                  21,
                  12,
                  20
                ]
              },
              "ticketCompleted": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "example": [
                  5,
                  10,
                  7,
                  3,
                  9,
                  6,
                  14,
                  17,
                  12,
                  18
                ]
              }
            }
          }
        }
      },
      "bodyUpdateUser": {
        "type": "object",
        "properties": {
          "_id": {
            "type": "string",
            "example": "5e2e91097df40e7ca045697d"
          },
          "userId": {
            "type": "string",
            "example": 960051
          },
          "applicationType": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "web",
              "app"
            ]
          },
          "createdAt": {
            "type": "string",
            "example": "2020-01-27T07:33:22.364Z"
          },
          "createdBy": {
            "type": "string",
            "example": 960051
          },
          "email": {
            "type": "string",
            "example": "960051@telkom.co.id"
          },
          "metaData": {
            "type": "object",
            "properties": {
              "nik": {
                "type": "string",
                "example": 960051
              },
              "email": {
                "type": "string",
                "example": "960051@telkom.co.id"
              },
              "fullName": {
                "type": "string",
                "example": "REYNALDO JOHANES"
              },
              "location": {
                "type": "string",
                "example": "SURABAYA"
              },
              "phoneNumber": {
                "type": "string",
                "example": "082139239328"
              },
              "segment": {
                "type": "string",
                "example": "DGS"
              },
              "company": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "example": ""
                  },
                  "name": {
                    "type": "string",
                    "example": ""
                  },
                  "category": {
                    "type": "string",
                    "example": ""
                  },
                  "subCategory": {
                    "type": "string",
                    "example": ""
                  }
                }
              },
              "ccHandled": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/ccHandledUpdate"
                },
                "example": [
                  {
                    "nipnas": 3223400,
                    "corporateClientName": "MASPION",
                    "segment": "IBS",
                    "location": "JATIM SURAMADU (SURABAYA)",
                    "witel": "JATIM SURAMADU (SURABAYA)",
                    "divre": 5,
                    "startHandled": 20191101,
                    "endHandled": 20191130
                  }
                ]
              },
              "divisionCode": {
                "type": "string",
                "example": ""
              },
              "division": {
                "type": "string",
                "example": ""
              },
              "unit": {
                "type": "string",
                "example": ""
              },
              "subUnit": {
                "type": "string",
                "example": ""
              },
              "jobTitle": {
                "type": "string",
                "example": "JAM 2"
              },
              "photo": {
                "type": "string",
                "example": ""
              },
              "nipnas": {
                "type": "integer",
                "example": null
              },
              "userApp": {
                "type": "object",
                "properties": {
                  "assurance": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string",
                        "example": "account_manager"
                      },
                      "isActive": {
                        "type": "boolean",
                        "example": true
                      }
                    }
                  },
                  "partnerObl": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string",
                        "example": ""
                      },
                      "isActive": {
                        "type": "boolean",
                        "example": false
                      }
                    }
                  },
                  "partnership": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string",
                        "example": ""
                      },
                      "isActive": {
                        "type": "boolean",
                        "example": false
                      }
                    }
                  },
                  "buying": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string",
                        "example": "account_manager"
                      },
                      "isActive": {
                        "type": "boolean",
                        "example": true
                      }
                    }
                  },
                  "delivery": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string",
                        "example": "account_manager"
                      },
                      "isActive": {
                        "type": "boolean",
                        "example": true
                      }
                    }
                  },
                  "catalogue": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string",
                        "example": "account_manager"
                      },
                      "isActive": {
                        "type": "boolean",
                        "example": true
                      }
                    }
                  }
                }
              }
            }
          },
          "nik": {
            "type": "string",
            "example": 960051
          },
          "password": {
            "type": "string",
            "example": ""
          },
          "salt": {
            "type": "string",
            "example": ""
          },
          "updatedAt": {
            "type": "string",
            "example": "2020-01-27T07:33:22.364Z"
          },
          "updatedBy": {
            "type": "string",
            "example": ""
          }
        }
      },
      "ccHandledUpdate": {
        "type": "object",
        "properties": {
          "nipnas": {
            "type": "integer"
          },
          "corporateClientName": {
            "type": "string"
          },
          "segment": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "witel": {
            "type": "string"
          },
          "divre": {
            "type": "string"
          },
          "startHandled": {
            "type": "string"
          },
          "endHandled": {
            "type": "string"
          }
        }
      },
      "bulkWrite400": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "message": {
            "type": "string",
            "example": "Bulk Write Mongo"
          },
          "code": {
            "type": "string",
            "example": 400
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "updateUser200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "string",
            "example": "OK"
          }
        }
      },
      "login": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "accessToken": {
                "type": "string"
              },
              "refreshToken": {
                "type": "string"
              },
              "accessTokenExpiresIn": {
                "type": "integer"
              },
              "refreshTokenExpiresIn": {
                "type": "integer"
              },
              "subscribe": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "role": {
                "type": "object",
                "properties": {
                  "roleId": {
                    "type": "string"
                  },
                  "roleName": {
                    "type": "string"
                  },
                  "roleChilds": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "roleId": {
                          "type": "string"
                        },
                        "roleName": {
                          "type": "string"
                        }
                      }
                    }
                  },
                  "apps": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "appId": {
                          "type": "string"
                        },
                        "appName": {
                          "type": "string"
                        }
                      }
                    }
                  }
                }
              },
              "photo": {
                "type": "string"
              },
              "fullName": {
                "type": "string"
              },
              "sub": {
                "type": "string"
              },
              "companyId": {
                "type": "string"
              },
              "ratingDate": {
                "type": "string"
              },
              "ratingStatus": {
                "type": "string"
              },
              "segment": {
                "type": "string"
              },
              "bud": {
                "type": "string"
              },
              "direktorat": {
                "type": "string"
              },
              "divisi": {
                "type": "string"
              },
              "unit": {
                "type": "string"
              },
              "privileges": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "category": {
                      "type": "string"
                    },
                    "feature": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string"
                          },
                          "function": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "Logout": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Logout Success"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "properties": {
              "email": {
                "type": "string",
                "example": "60127@telkom.co.id"
              },
              "fullName": {
                "type": "string",
                "example": "IMAM SUTRISNO"
              },
              "role": {
                "type": "string",
                "example": "engineer_on_site"
              },
              "nik": {
                "type": "integer",
                "example": 60127
              }
            }
          }
        }
      },
      "eosCreateTicket": {
        "type": "object",
        "properties": {
          "nipnas": {
            "type": "string",
            "example": 5588375
          },
          "corporateClientName": {
            "type": "string",
            "example": "BANK RAKYAT INDONESIA (PERSERO)"
          },
          "serviceCategory": {
            "type": "string",
            "example": "CONNECTIVITY"
          },
          "sid": {
            "type": "string",
            "example": "12345TES2"
          },
          "type": {
            "type": "string",
            "example": "fault_ticket"
          },
          "ipWan": {
            "type": "integer",
            "example": 1234567890
          },
          "location": {
            "type": "string",
            "example": "Jln Cihanjuang, Cimahi, Jawa Barat"
          },
          "serviceId": {
            "type": "string",
            "example": "VPNIP_NODE"
          },
          "serviceName": {
            "type": "string",
            "example": "Astinet 100M"
          },
          "symptomId": {
            "type": "string",
            "example": "symp-B01001"
          },
          "complaint": {
            "type": "string",
            "example": "Nelpon ke KPK tapi nyambung nya ke Vanessa Angel, tolong fix segera ada yang korupsi di kantor kades"
          },
          "node": {
            "type": "string",
            "example": "PE-D3-LBG-VPN"
          },
          "interfaces": {
            "type": "string",
            "example": "Gi0/7/0/10.3610"
          },
          "description": {
            "type": "string",
            "example": "470089-0029677009 VPN IP KIMIA FARMA Jl Cihampelas No 5 Bandung"
          },
          "attachment": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/attachType"
            },
            "example": [
              {
                "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
              },
              {
                "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
              },
              {
                "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
              }
            ]
          },
          "picName": {
            "type": "string",
            "example": "Arnold"
          },
          "picPhoneNumber": {
            "type": "integer",
            "example": "0821123456789"
          }
        }
      },
      "attachType": {
        "type": "object",
        "properties": {
          "image": {
            "type": "string"
          }
        }
      },
      "FormCreateTicketConn": {
        "type": "object",
        "properties": {
          "nipnas": {
            "type": "string",
            "example": 5588375
          },
          "custAccntName": {
            "type": "string",
            "example": "BANK RAKYAT INDONESIA (PERSERO)"
          },
          "serviceCategory": {
            "type": "string",
            "example": "CONNECTIVITY"
          },
          "sid": {
            "type": "string",
            "example": "12345TES2"
          },
          "ipWan": {
            "type": "integer",
            "example": 1234567890
          },
          "location": {
            "type": "string",
            "example": "Jln Cihanjuang, Cimahi, Jawa Barat"
          },
          "serviceId": {
            "type": "string",
            "example": "VPNIP_NODE"
          },
          "serviceName": {
            "type": "string",
            "example": "Astinet 100M"
          },
          "symptomId": {
            "type": "string",
            "example": "symp-B01001"
          },
          "complaint": {
            "type": "string",
            "example": "Nelpon ke KPK tapi nyambung nya ke Vanessa Angel, tolong fix segera ada yang korupsi di kantor kades"
          },
          "picName": {
            "type": "string",
            "example": "Arnold"
          },
          "picPhoneNumber": {
            "type": "integer",
            "example": "0821123456789"
          }
        }
      },
      "200TicketAM": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "ticketId": {
                "type": "string",
                "example": "TDS-181206085424101024"
              },
              "ticketNossa": {
                "type": "string",
                "example": "Validasi"
              },
              "ticketMyCx": {
                "type": "string",
                "example": 45662
              },
              "userId": {
                "type": "string",
                "example": 558682012121801
              },
              "categoryId": {
                "type": "string",
                "example": "E001"
              },
              "serviceId": {
                "type": "string",
                "example": "VPNIP_NODE"
              },
              "serviceName": {
                "type": "string",
                "example": "Astinet 100 Mbps"
              },
              "location": {
                "type": "string",
                "example": "Jl Sunan Kalijaga, Jambi"
              },
              "symptomId": {
                "type": "string",
                "example": "symp-A01001"
              },
              "complaint": {
                "type": "string",
                "example": "Tidak bisa internetan padahal semua led di STB sudah oke"
              },
              "ticketPublish": {
                "type": "object",
                "example": {
                }
              },
              "worklog": {
                "type": "object",
                "example": {
                }
              },
              "ticketCompleted": {
                "type": "object",
                "example": {
                }
              },
              "status": {
                "type": "string",
                "example": "Validasi"
              },
              "picName": {
                "type": "string",
                "example": "Jang Ki Young"
              },
              "picPhoneNumber": {
                "type": "string",
                "example": "082326066070"
              },
              "createdAt": {
                "type": "string",
                "format": "date-time",
                "example": "14/10/2018 - 14:48"
              },
              "updatedAt": {
                "type": "string",
                "format": "date-time",
                "example": "14/10/2018 - 14:48"
              },
              "nipnas": {
                "type": "integer",
                "example": 5588375
              },
              "custAccntNum": {
                "type": "string",
                "example": 1280502
              },
              "ipWan": {
                "type": "integer",
                "example": ""
              }
            }
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "code": {
            "type": "string",
            "example": 200
          }
        }
      },
      "CreateTicket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "ticketId": {
                "type": "string",
                "example": "TDS-181206085424101024"
              },
              "ticketNossa": {
                "type": "string",
                "example": "Validasi"
              },
              "ticketMyCx": {
                "type": "string",
                "example": 45662
              },
              "userId": {
                "type": "string",
                "example": 558682012121801
              },
              "type": {
                "type": "string",
                "example": "fault_ticket"
              },
              "categoryId": {
                "type": "string",
                "example": "E001"
              },
              "serviceId": {
                "type": "string",
                "example": "VPNIP_NODE"
              },
              "serviceName": {
                "type": "string",
                "example": "Astinet 100 Mbps"
              },
              "location": {
                "type": "string",
                "example": "Jl Sunan Kalijaga, Jambi"
              },
              "symptomId": {
                "type": "string",
                "example": "symp-A01001"
              },
              "complaint": {
                "type": "string",
                "example": "Tidak bisa internetan padahal semua led di STB sudah oke"
              },
              "ticketPublish": {
                "type": "object",
                "example": {
                }
              },
              "worklog": {
                "type": "object",
                "example": {
                }
              },
              "ticketCompleted": {
                "type": "object",
                "example": {
                }
              },
              "status": {
                "type": "string",
                "example": "Validasi"
              },
              "node": {
                "type": "string",
                "example": "PE-D3-LBG-VPN"
              },
              "interfaces": {
                "type": "string",
                "example": "Gi0/7/0/10.3610"
              },
              "description": {
                "type": "string",
                "example": "470089-0029677009 VPN IP KIMIA FARMA Jl Cihampelas No 5 Bandung"
              },
              "picName": {
                "type": "string",
                "example": "Jang Ki Young"
              },
              "picPhoneNumber": {
                "type": "string",
                "example": "082326066070"
              },
              "createdAt": {
                "type": "string",
                "format": "date-time",
                "example": "14/10/2018 - 14:48"
              },
              "updatedAt": {
                "type": "string",
                "format": "date-time",
                "example": "14/10/2018 - 14:48"
              },
              "nipnas": {
                "type": "integer",
                "example": 5588375
              },
              "custAccntNum": {
                "type": "string",
                "example": 1280502
              },
              "npsShow": {
                "type": "boolean",
                "example": false
              },
              "nik": {
                "type": "integer",
                "example": 60127
              }
            }
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "code": {
            "type": "string",
            "example": 200
          }
        }
      },
      "FormCreateTicketNonConn": {
        "type": "object",
        "properties": {
          "custAccntName": {
            "type": "string",
            "example": "BANK RAKYAT INDONESIA (PERSERO)"
          },
          "serviceCategory": {
            "type": "string",
            "example": "NON-CONNECTIVITY"
          },
          "sid": {
            "type": "string",
            "example": "SID tidak ditemukan"
          },
          "location": {
            "type": "string",
            "example": "Jln Cihanjuang, Cimahi, Jawa Barat"
          },
          "serviceName": {
            "type": "string",
            "example": "Astinet 100M"
          },
          "deviceName": {
            "type": "string",
            "example": "HT-175"
          },
          "deviceId": {
            "type": "string",
            "example": "PC04NYEE"
          },
          "deviceSeriesNumber": {
            "type": "string",
            "example": 24010310110038
          },
          "symptomId": {
            "type": "string",
            "example": "symp-B01001"
          },
          "complaint": {
            "type": "string",
            "example": "Nelpon ke KPK tapi nyambung nya ke Vanessa Angel, tolong fix segera ada yang korupsi di kantor kades"
          },
          "picName": {
            "type": "string",
            "example": "Arnold"
          },
          "picPhoneNumber": {
            "type": "integer",
            "example": "0821123456789"
          }
        }
      },
      "CreateTicketNonConn": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "ticketId": {
                "type": "string",
                "example": "TDS-181206085424101024"
              },
              "ticketNossa": {
                "type": "string",
                "example": "Validasi"
              },
              "ticketMyCx": {
                "type": "string",
                "example": 45662
              },
              "userId": {
                "type": "string",
                "example": 558682012121801
              },
              "categoryId": {
                "type": "string",
                "example": "E001"
              },
              "serviceId": {
                "type": "string",
                "example": "VPNIP_NODE"
              },
              "serviceName": {
                "type": "string",
                "example": "Astinet 100 Mbps"
              },
              "location": {
                "type": "string",
                "example": "Jl Sunan Kalijaga, Jambi"
              },
              "deviceName": {
                "type": "string",
                "example": "HT-175"
              },
              "deviceId": {
                "type": "string",
                "example": "PC04NYEE"
              },
              "deviceSeriesNumber": {
                "type": "string",
                "example": 24010310110038
              },
              "symptomId": {
                "type": "string",
                "example": "symp-B01001"
              },
              "complaint": {
                "type": "string",
                "example": "Perangkat rusak"
              },
              "ticketPublish": {
                "type": "string",
                "example": {
                }
              },
              "worklog": {
                "type": "string",
                "example": {
                }
              },
              "ticketCompleted": {
                "type": "string",
                "example": {
                }
              },
              "status": {
                "type": "string",
                "example": "Validasi"
              },
              "picName": {
                "type": "string",
                "example": "Jang Ki Young"
              },
              "picPhoneNumber": {
                "type": "string",
                "example": "082326066070"
              },
              "createdAt": {
                "type": "string",
                "format": "date-time",
                "example": "14/10/2018 - 14:48"
              },
              "updateAt": {
                "type": "string",
                "format": "date-time",
                "example": "14/10/2018 - 14:48"
              },
              "nipnas": {
                "type": "integer",
                "example": 5588375
              },
              "custAccntNum": {
                "type": "string",
                "example": 1280502
              },
              "npsShow": {
                "type": "boolean",
                "example": false
              },
              "nik": {
                "type": "integer",
                "example": 60127
              }
            }
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "code": {
            "type": "string",
            "example": 200
          }
        }
      },
      "nok401Login": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "string",
            "example": 401
          },
          "message": {
            "type": "string",
            "example": "Authentication information is missing or invalid."
          },
          "data": {
          }
        }
      },
      "nok400Login": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "string",
            "example": 400
          },
          "message": {
            "type": "string",
            "example": "Your account has been logged-in in another device."
          },
          "data": {
          }
        }
      },
      "409LoginResponse": {
        "type": "object",
        "oneOf": [
          {
            "$ref": "#/components/schemas/409LoginResponse1"
          },
          {
            "$ref": "#/components/schemas/409LoginResponse2"
          },
          {
            "$ref": "#/components/schemas/409LoginResponse3"
          }
        ]
      },
      "409LoginResponse1": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "string",
            "example": 409
          },
          "message": {
            "type": "string",
            "example": "Password must contain alpha-numeric characters"
          },
          "data": {
          }
        }
      },
      "409LoginResponse2": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "string",
            "example": 409
          },
          "message": {
            "type": "string",
            "example": "Conflict"
          },
          "data": {
            "type": "string",
            "example": {
            }
          }
        }
      },
      "409LoginResponse3": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "string",
            "example": 409
          },
          "message": {
            "type": "string",
            "example": "Password is not allowed to be empty"
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "nok500Login": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "string",
            "example": 500
          },
          "message": {
            "type": "string",
            "example": "Can not do login, system fault."
          },
          "data": {
          }
        }
      },
      "nok500Internal": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "code": {
            "type": "integer",
            "example": 500
          },
          "message": {
            "type": "string",
            "example": "Internal Server Error"
          },
          "data": {
          }
        }
      },
      "listCA": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "oke"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CAData"
            },
            "example": [
              {
                "_id": "5c52a61e4a0d160010778096",
                "nipnas": 2191828,
                "custAccountNum": 5586925,
                "corporateAccounttName": "BANK BENGKULU",
                "segment": "BMS-2",
                "location": "BENGKULU",
                "witel": "BENGKULU",
                "divre": 1
              }
            ]
          }
        }
      },
      "CAData": {
        "type": "object",
        "properties": {
          "_id": {
            "type": "string"
          },
          "nipnas": {
            "type": "string"
          },
          "custAccountNum": {
            "type": "string"
          },
          "corporateAccounttName": {
            "type": "string"
          },
          "segment": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "witel": {
            "type": "string"
          },
          "divre": {
            "type": "string"
          }
        }
      },
      "ListNipnasAM": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "nipnas": {
                  "type": "integer"
                },
                "corporateClientName": {
                  "type": "string"
                },
                "serviceCount": {
                  "type": "integer"
                },
                "servicePoint": {
                  "type": "integer"
                }
              }
            }
          }
        }
      },
      "listCAAM": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "oke"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataCA"
            },
            "example": [
              {
                "_id": "5c732f05c13e8f0010d486ca",
                "custAccntName": "BANK RAKYAT INDONESIA (PERSERO)",
                "custAccntNum": 1278012,
                "divre": 2,
                "location": "KW JAKARTA SELATAN",
                "nipnas": 3705763,
                "segment": "BMS-1",
                "witel": "JAKARTA SELATAN"
              }
            ]
          }
        }
      },
      "Profile": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": ""
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "properties": {
              "_id": {
                "type": "string",
                "example": "5c937075cdac633059b5c6dd"
              },
              "userId": {
                "type": "string",
                "example": 850094
              },
              "email": {
                "type": "string",
                "example": "850094@telkom.co.id"
              },
              "password": {
                "type": "string",
                "example": "08f91435299c64d870d3309d4c6d83b05e8c50449e29f72da3a99a04d11b1a02fd9eede63fea798cd5af2647f087aafb28db25bccca41ae555c40b982afa2524"
              },
              "role": {
                "type": "string",
                "example": "account_manager"
              },
              "createdAt": {
                "type": "string",
                "example": "2019-03-21T11:07:32.745Z"
              },
              "updatedAt": {
                "type": "string",
                "example": "2019-03-21T11:07:32.745Z"
              },
              "data": {
                "type": "object",
                "properties": {
                  "nik": {
                    "type": "string",
                    "example": 850094
                  },
                  "fullName": {
                    "type": "string",
                    "example": "SANDRA FITRI ASTRINI, MM"
                  },
                  "location": {
                    "type": "string",
                    "example": "SOLO"
                  },
                  "ccHandled": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/DataCA"
                    },
                    "example": [
                      {
                        "nipnas": 4602791,
                        "corporateClientName": "IAIN SURAKARTA",
                        "segment": "EMS",
                        "location": "JATENG TIMUR SELATAN (SOLO)",
                        "witel": "JATENG TIMUR SELATAN (SOLO)",
                        "divre": 4,
                        "employees": [
                          {
                            "email": "00081047@eosdestelkom.id",
                            "role": "engineer_on_site",
                            "data": {
                              "nik": "00081047",
                              "fullName": "ANGGA PRAYOGA ADI KUNCORO",
                              "phoneNumber": "081299392547"
                            },
                            "photoProfile": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                          }
                        ]
                      },
                      {
                        "nipnas": 2000006,
                        "corporateClientName": "INSTITUT SENI INDONESIA SURAKARTA",
                        "segment": "EMS",
                        "location": "JATENG TIMUR SELATAN (SOLO)",
                        "witel": "JATENG TIMUR SELATAN (SOLO)",
                        "divre": 4,
                        "employees": [

                        ]
                      },
                      {
                        "nipnas": 2000267,
                        "corporateClientName": "UNIVERSITAS MUHAMMADIYAH SURAKARTA",
                        "segment": "EMS",
                        "location": "JATENG TIMUR SELATAN (SOLO)",
                        "witel": "JATENG TIMUR SELATAN (SOLO)",
                        "divre": 4,
                        "engineer_on_site": [

                        ]
                      },
                      {
                        "nipnas": 5587668,
                        "corporateClientName": "UNIVERSITAS MUHAMMADIYAH SURAKARTA",
                        "segment": "EMS",
                        "location": "JATENG TIMUR SELATAN (SOLO)",
                        "witel": "JATENG TIMUR SELATAN (SOLO)",
                        "divre": 4,
                        "engineer_on_site": [

                        ]
                      },
                      {
                        "nipnas": 5588375,
                        "corporateClientName": "KONIMEX PT",
                        "segment": "HWS",
                        "location": "JATENG TIMUR SELATAN (SOLO)",
                        "witel": "JATENG TIMUR SELATAN (SOLO)",
                        "divre": 4,
                        "engineer_on_site": [
                          {
                            "_id": "5c937093cdac633059b5c7f9",
                            "userId": "00041969",
                            "email": "00041969@telkom.co.id",
                            "role": "engineer_on_site",
                            "data": {
                              "nik": "00041969",
                              "fullName": "ANANG SETIAWAN",
                              "phoneNumber": "082133765756",
                              "gender": "LAKI-LAKI",
                              "birthPlace": "SEMARANG",
                              "birthDate": "",
                              "comeIn": "",
                              "nameSPV": "AHMAD MEGANESHA",
                              "noSPV": "081210375887",
                              "emailSPV": "a.meganesha@gmail.com",
                              "segment": "MAS",
                              "active": "AKTIF",
                              "total": 1
                            },
                            "photoProfile": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                          }
                        ]
                      },
                      {
                        "nipnas": 10215607,
                        "corporateClientName": "ORTOPEDI SURAKARTA",
                        "segment": "HWS",
                        "location": "JATENG TIMUR SELATAN (SOLO)",
                        "witel": "JATENG TIMUR SELATAN (SOLO)",
                        "divre": 4,
                        "engineer_on_site": [

                        ]
                      },
                      {
                        "nipnas": 2938824,
                        "corporateClientName": "ANGKASAPURA I",
                        "segment": "TMS",
                        "location": "JAKARTA PUSAT",
                        "witel": "JAKARTA PUSAT",
                        "divre": 5,
                        "engineer_on_site": [
                          {
                            "_id": "5c937093cdac633059b5c7ca",
                            "userId": 31197,
                            "email": "00074735@telkom.co.id",
                            "role": "engineer_on_site",
                            "data": {
                              "nik": 31197,
                              "fullName": "FRANS HARDY NATANAEL SITORUS",
                              "phoneNumber": "081269670322",
                              "gender": "LAKI-LAKI",
                              "birthPlace": "MEDAN",
                              "birthDate": "",
                              "comeIn": "",
                              "nameSPV": "MUAMMAR RUSLY",
                              "noSPV": "081310977171",
                              "emailSPV": "ammarco.milano@gmail.com",
                              "segment": "TMS",
                              "active": "AKTIF",
                              "total": 1,
                              "handlerLog": {
                                "deviceId": "12asda",
                                "tokenfcm": "test"
                              }
                            },
                            "photoProfile": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                          },
                          {
                            "_id": "5c937093cdac633059b5c8c3",
                            "userId": "00084704",
                            "email": "00084704@telkom.co.id",
                            "role": "engineer_on_site",
                            "data": {
                              "nik": "00084704",
                              "fullName": "NI NYOMAN DESY WAHYUNI",
                              "phoneNumber": "081238314639",
                              "gender": "PEREMPUAN",
                              "birthPlace": "DENPASAR",
                              "birthDate": "",
                              "comeIn": "",
                              "nameSPV": "FITYAH FULKI FURQAN",
                              "noSPV": "081382290303",
                              "emailSPV": "fityahfulki@gmail.com",
                              "segment": "AREA",
                              "active": "AKTIF",
                              "total": 1
                            },
                            "photoProfile": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                          },
                          {
                            "_id": "5c937093cdac633059b5c8c4",
                            "userId": "00030944",
                            "email": "00030944@telkom.co.id",
                            "role": "engineer_on_site",
                            "data": {
                              "nik": "00030944",
                              "fullName": "I GEDE BUDHI INDRAWAN",
                              "phoneNumber": "081286153020",
                              "gender": "LAKI-LAKI",
                              "birthPlace": "KARANGASEM",
                              "birthDate": "",
                              "comeIn": "",
                              "nameSPV": "MUAMMAR RUSLY",
                              "noSPV": "081310977171",
                              "emailSPV": "ammarco.milano@gmail.com",
                              "segment": "TMS",
                              "active": "AKTIF",
                              "total": 1
                            },
                            "photoProfile": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
                          }
                        ]
                      }
                    ]
                  },
                  "handlerLog": {
                    "type": "object",
                    "properties": {
                      "deviceId": {
                        "type": "string",
                        "example": "12asda"
                      },
                      "tokenfcm": {
                        "type": "string",
                        "example": "test"
                      }
                    }
                  },
                  "phoneNumber": {
                    "type": "string",
                    "example": "081329350920"
                  }
                }
              }
            }
          }
        }
      },
      "dataNipnas": {
        "type": "object",
        "properties": {
          "_id": {
            "type": "string"
          },
          "nipnas": {
            "type": "string"
          },
          "custAccountNum": {
            "type": "string"
          },
          "corporateAccounttName": {
            "type": "string"
          },
          "segment": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "witel": {
            "type": "string"
          },
          "divre": {
            "type": "string"
          }
        }
      },
      "DataCA": {
        "type": "object",
        "properties": {
          "_id": {
            "type": "string"
          },
          "custAccntName": {
            "type": "string"
          },
          "custAccntNum": {
            "type": "string"
          },
          "divre": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "nipnas": {
            "type": "integer"
          },
          "segment": {
            "type": "string"
          },
          "witel": {
            "type": "string"
          },
          "engineer_on_site": {
            "type": "string"
          }
        }
      },
      "ListPortofolioCustomer": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "properties": {
              "custName": {
                "type": "string",
                "example": "DUTA ANGGADA REALTY"
              },
              "address": {
                "type": "string",
                "example": "JAKARTA PUSAT"
              },
              "portofolio": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/PortofolioCustomer"
                },
                "example": [
                  {
                    "product": "VPN IP",
                    "product_alias": "VPN IP",
                    "listProduct": [
                      {
                        "service id": " ",
                        "servicename": "MM_VPNIP_RL1",
                        "packagename": "0.125MBPS",
                        "addr": "PT BATAVIA FINANCE-JL. PASAR I RING ROAD"
                      },
                      {
                        "service id": "4700012-0001523259",
                        "servicename": "MM_VPNIP_RL1",
                        "packagename": "0.5MBPS",
                        "addr": "PT SEWU SEGAR NUSANTARA-jl kopo permai Ijl kopo permai I Blk 55A 12     KPO"
                      },
                      {
                        "service id": "4700012-0001524596",
                        "servicename": "MM_VPNIP_RL1",
                        "packagename": "0.125MBPS",
                        "addr": "PT SINARMAS MULTIFINANCE-Jl MuhidinRuko SUTOS Sungai Liat Town Square No C3     SLT"
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      },
      "PortofolioCustomer": {
        "type": "object",
        "properties": {
          "product": {
            "type": "string"
          },
          "product_alias": {
            "type": "string"
          },
          "listProduct": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ListProduct"
            }
          }
        }
      },
      "ListProduct": {
        "type": "object",
        "properties": {
          "service id": {
            "type": "string"
          },
          "servicename": {
            "type": "string"
          },
          "packagename": {
            "type": "string"
          },
          "addr": {
            "type": "string"
          }
        }
      },
      "listOrderNipnas": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataMrtg"
            },
            "example": [
              {
                "sid": 1279358,
                "serviceName": "Manage Network",
                "location": "Ds. KARANGREJA PURBOLINGGO JAWA TENGAH,-,Purbolinggo,99999"
              },
              {
                "sid": "04702581",
                "serviceName": "Manage Network",
                "location": "Ds. SUKABUMI KEC. CEPOGO  BOYOLALI  JAWA TENGAH,-,Boyolali,99999"
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 2
              },
              "totalPage": {
                "type": "integer",
                "example": 138
              },
              "totalData": {
                "type": "integer",
                "example": 275
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          }
        }
      },
      "ListAMOrder": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "properties": {
              "custAccntName": {
                "type": "string",
                "example": "DUTA ANGGADA REALTY"
              },
              "custAccntNum": {
                "type": "string",
                "example": 329282373
              },
              "address": {
                "type": "string",
                "example": "JAKARTA PUSAT"
              },
              "portofolio": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Portofolio"
                },
                "example": [
                  {
                    "product": "VPN IP",
                    "product_alias": "VPN IP",
                    "listProduct": [
                      {
                        "service id": "4700012-0001531625",
                        "servicename": "MM_VPNIP_RL1",
                        "packagename": "0.125MBPS",
                        "serviceCategory": "CONNECTIVITY",
                        "addr": "PT SINARMAS MULTIFINANCE-JL JEND SUDIRMAN ktr Cabang Sinarmas Multifinance CM"
                      }
                    ]
                  }
                ]
              }
            }
          }
        }
      },
      "Portofolio": {
        "type": "object",
        "properties": {
          "product": {
            "type": "string"
          },
          "product_alias": {
            "type": "string"
          },
          "listProduct": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Portofolio1"
            }
          }
        }
      },
      "Portofolio1": {
        "type": "object",
        "properties": {
          "service id": {
            "type": "string"
          },
          "servicename": {
            "type": "string"
          },
          "serviceCategory": {
            "type": "string"
          },
          "addr": {
            "type": "string"
          }
        }
      },
      "Symptoms": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SymptomsCategory"
            },
            "example": [
              {
                "symptomcode": "C_CONN \\\\ C_CONN_001 \\\\ C_CONN_001_001 \\\\ C_CONN_001_001_001",
                "symptomname": "Mati Total Fisik"
              }
            ]
          }
        }
      },
      "SymptomsCategory": {
        "type": "object",
        "properties": {
          "symptomcode": {
            "type": "string"
          },
          "symptomname": {
            "type": "string"
          }
        }
      },
      "ticketOtherChannel": {
        "type": "object",
        "properties": {
          "EXTTransactionID": {
            "type": "string",
            "example": "190612-108994"
          },
          "assetNum": {
            "type": "string",
            "example": "41324943_162504218635_IPTV"
          },
          "contactName": {
            "type": "string",
            "example": "ISAK WANAMOB"
          },
          "contactPhone": {
            "type": "string",
            "example": "082250189082"
          },
          "externalSystem": {
            "type": "string",
            "example": "RIGHTNOW"
          },
          "gaul": {
            "type": "string",
            "example": ""
          },
          "hardComplaint": {
            "type": "string",
            "example": ""
          },
          "longDescription": {
            "type": "string",
            "example": "iptv belum terpasang, petugas belum datang lg sampe dengan hari ini. mohon segera dibantu segera dipasang"
          },
          "lapul": {
            "type": "string",
            "example": ""
          },
          "urgensi": {
            "type": "string",
            "example": ""
          },
          "ticketType": {
            "type": "string",
            "example": "TEKNIKAL"
          },
          "idReference": {
            "type": "string",
            "example": "190612-108994"
          },
          "symptomID": {
            "type": "string",
            "example": 15769
          },
          "TKCUSTOMERSEGMENT": {
            "type": "string",
            "example": "DCS"
          },
          "TK_TICKET_05": {
            "type": "string",
            "example": ""
          },
          "TK_TICKET_16": {
            "type": "string",
            "example": ""
          },
          "TK_TICKET_19": {
            "type": "string",
            "example": "USEEENTRYH (HD)"
          },
          "TK_TICKET_20": {
            "type": "string",
            "example": ""
          },
          "TK_TICKET_23": {
            "type": "string",
            "example": "100 - Residensial"
          },
          "TK_TICKET_27": {
            "type": "string",
            "example": ""
          },
          "TK_TICKET_28": {
            "type": "string",
            "example": ""
          },
          "TK_TICKET_39": {
            "type": "string",
            "example": ""
          },
          "ticketID": {
            "type": "string",
            "example": "IN52241672"
          },
          "gamasID": {
            "type": "integer",
            "example": 543251
          },
          "owner": {
            "type": "string",
            "example": ""
          },
          "ownerGroup": {
            "type": "string",
            "example": ""
          },
          "reportedBy": {
            "type": "string",
            "example": "LIA.RISMAWATI"
          },
          "reportDate": {
            "type": "string",
            "example": "2019-06-12T10:25:36.135904+07:00"
          }
        }
      },
      "ticketOtherChannel200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "worklogRead": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Worklog updated"
          },
          "data": {
            "type": "string",
            "example": "OK"
          }
        }
      },
      "createTicketAM": {
        "type": "object",
        "properties": {
          "categoryId": {
            "type": "string",
            "example": "E001"
          },
          "serviceId": {
            "type": "string",
            "example": "VPNIP_NODE"
          },
          "serviceCategory": {
            "type": "string",
            "example": "Connectivity"
          },
          "serviceName": {
            "type": "string",
            "example": "MPLS VPN IP Node"
          },
          "location": {
            "type": "string",
            "example": "PLN ( PERSERO ) SEKTOR BAKARU JL. H. A. MUHAMMAD ARSYAD, SOREANG, PAREPARE,21,1,PLN PEMBANGKIT BAKARU"
          },
          "sid": {
            "type": "string",
            "example": "4700000-0030917097"
          },
          "ipWan": {
            "type": "string",
            "example": null
          },
          "symptomId": {
            "type": "string",
            "example": "C_CONN \\\\ C_CONN_001 \\\\ C_CONN_001_001 \\\\ C_CONN_001_001_002"
          },
          "symptompsName": {
            "type": "string",
            "example": "Mati Logic"
          },
          "complaint": {
            "type": "string",
            "example": "Mati sudah 1 jam"
          },
          "picName": {
            "type": "string",
            "example": "Novi"
          },
          "picPhoneNumber": {
            "type": "string",
            "example": "082326066070"
          },
          "nipnas": {
            "type": "integer",
            "example": 1405567
          }
        }
      },
      "ListTicket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ticketData"
            },
            "example": [
              {
                "ticketId": "TDS-123tes161554709075539",
                "id": "INTes001",
                "category": "E001",
                "serviceId": "4700709-0030894845",
                "serviceName": "MM_ASTINET",
                "corporateClientName": "PT. PERTAMINA",
                "location": "Jln Cihanjuang, Cimahi, Jawa Barat",
                "complaint": "Tidak bisa internetan padahal semua led di STB sudah oke",
                "status": "Tiket Terbit",
                "createdAt": "2019-04-07T14:38:00.734Z",
                "rating": {
                }
              },
              {
                "ticketId": "TDS-undefined1554644338343",
                "id": "IOSTes01",
                "category": "",
                "serviceId": "4700709-0031099886",
                "serviceName": "MM_ASTINET",
                "corporateClientName": "PT. PLN",
                "location": "Jakarta",
                "complaint": "[922283773/mas zul/+62 81907275727] [GANGGUAN][DES][ASTINETLITE] 922283773 Indomart toko TDFF jl rinjani praya layanan down [C_CONN][TOP200][DES]",
                "status": "Selesai",
                "createdAt": "2019-04-07T20:39:00.734Z",
                "rating": {
                  "value": 5,
                  "dateTime": "2019-04-08T08:00:47.734Z",
                  "message": "Tes"
                }
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 10
              },
              "totalPage": {
                "type": "integer",
                "example": 1
              },
              "totalData": {
                "type": "integer",
                "example": 2
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success get list ticket"
          }
        }
      },
      "ticketData": {
        "type": "object",
        "properties": {
          "ticketId": {
            "type": "string",
            "example": true
          },
          "id": {
            "type": "string"
          },
          "category": {
            "type": "string"
          },
          "serviceId": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "complaint": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "createdAt": {
            "type": "string"
          },
          "rating": {
            "type": "object",
            "properties": {
              "value": {
                "type": "integer"
              },
              "dateTime": {
                "type": "string"
              },
              "message": {
                "type": "string"
              }
            }
          }
        }
      },
      "bodyAddWorklog": {
        "type": "object",
        "properties": {
          "ticketId": {
            "type": "string",
            "example": "IN250819"
          },
          "summary": {
            "type": "string",
            "example": "Mohon bantuan redispatch ke C4DES"
          },
          "detail": {
            "type": "string",
            "example": "Call PIC Bpk. Yahya. Mohon bantuannya untuk konfirmasi kembali"
          },
          "attachment": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              {
                "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
              },
              {
                "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
              },
              {
                "image": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
              }
            ]
          }
        }
      },
      "200AddWorklog": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "worklog200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/worklogType"
            },
            "example": [
              {
                "ticketId": "IN250819",
                "count": 2,
                "from": "mytds",
                "createdAt": "2019-04-07T14:38:00.734Z",
                "isRead": false
              },
              {
                "ticketId": "IN673665",
                "count": 0,
                "from": "mytds",
                "createdAt": "2019-04-07T15:38:00.734Z",
                "isRead": true
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 10
              },
              "totalPage": {
                "type": "integer",
                "example": 1
              },
              "totalData": {
                "type": "integer",
                "example": 2
              }
            }
          }
        }
      },
      "worklogType": {
        "type": "object",
        "properties": {
          "ticketId": {
            "type": "string"
          },
          "count": {
            "type": "integer"
          },
          "dateTime": {
            "type": "string"
          },
          "isRead": {
            "type": "boolean"
          }
        }
      },
      "worklogDetail200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/worklogDetailType"
            },
            "example": [
              {
                "worklogId": 649301,
                "createdBy": "IJ25081",
                "createdAt": "2019-11-22T14:38:00.734Z",
                "summary": "Konfirmasi Layanan",
                "userId": "",
                "isRead": true,
                "detail": {
                  "type": "AGENTNOTE",
                  "class": "INCIDENT",
                  "description": "Call PIC Bpk. Yaya 0811311818 >>> RNA. Mohon bantuannya untuk konfirmasi kembali, rekan. Terimakasih",
                  "longDescription": "nomor alternatif&amp;nbsp;081282133196"
                }
              },
              {
                "worklogId": 649302,
                "createdBy": "IJ25081",
                "createdAt": "2019-11-22T14:38:00.734Z",
                "summary": "Konfirmasi Layanan",
                "userId": "",
                "isRead": true,
                "detail": {
                  "type": "AGENTNOTE",
                  "class": "INCIDENT",
                  "description": "Call PIC Bpk. Yaya 0811311818 >>> RNA. Mohon bantuannya untuk konfirmasi kembali, rekan. Terimakasih",
                  "longDescription": "nomor alternatif&amp;nbsp;081282133196"
                }
              },
              {
                "worklogId": 649303,
                "createdBy": "IJ25081",
                "createdAt": "2019-11-21T14:38:00.734Z",
                "summary": "Konfirmasi Layanan",
                "detail": {
                  "type": "AGENTNOTE",
                  "class": "INCIDENT",
                  "description": "Call PIC Bpk. Yaya 0811311818 >>> RNA. Mohon bantuannya untuk konfirmasi kembali, rekan. Terimakasih",
                  "longDescription": "nomor alternatif&amp;nbsp;081282133196"
                }
              },
              {
                "worklogId": 154672,
                "createdBy": "IJ25081",
                "createdAt": "2019-11-17T14:38:00.734Z",
                "summary": "Konfirmasi Layanan",
                "userId": "",
                "isRead": true,
                "detail": {
                  "type": "AGENTNOTE",
                  "class": "INCIDENT",
                  "description": "Call PIC Bpk. Yaya 0811311818 >>> RNA. Mohon bantuannya untuk konfirmasi kembali, rekan. Terimakasih",
                  "longDescription": "nomor alternatif&amp;nbsp;081282133196"
                }
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 10
              },
              "totalPage": {
                "type": "integer",
                "example": 1
              },
              "totalData": {
                "type": "integer",
                "example": 2
              }
            }
          }
        }
      },
      "worklogDetailType": {
        "type": "object",
        "properties": {
          "createdBy": {
            "type": "string"
          },
          "dateTime": {
            "type": "string"
          },
          "summary": {
            "type": "string"
          },
          "userId": {
            "type": "string"
          },
          "isRead": {
            "type": "boolean"
          },
          "detail": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string"
              },
              "class": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "longDescription": {
                "type": "string"
              }
            }
          }
        }
      },
      "countWorklog": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Result for count chat"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "integer",
            "example": 1
          }
        }
      },
      "request200get": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "corporateClientName": {
                "type": "string"
              },
              "serviceCategory": {
                "type": "string"
              },
              "sid": {
                "type": "string"
              },
              "ipWan": {
                "type": "string"
              },
              "location": {
                "type": "string"
              },
              "serviceName": {
                "type": "string"
              },
              "defaultSymptom": {
                "type": "string"
              },
              "symptom": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "symptomId": {
                      "type": "string"
                    },
                    "symptomDescription": {
                      "type": "string"
                    }
                  }
                }
              },
              "complaint": {
                "type": "string"
              },
              "node": {
                "type": "string"
              },
              "interface": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "picName": {
                "type": "string"
              },
              "picPhoneNumber": {
                "type": "string"
              }
            }
          }
        }
      },
      "bodyApprove": {
        "type": "object",
        "properties": {
          "ticketId": {
            "type": "string"
          },
          "corporateClientName": {
            "type": "string"
          },
          "serviceCategory": {
            "type": "string"
          },
          "sid": {
            "type": "string"
          },
          "ipWan": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "symptomId": {
            "type": "string"
          },
          "symptomName": {
            "type": "string"
          },
          "complaint": {
            "type": "string"
          },
          "node": {
            "type": "string"
          },
          "interface": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "picName": {
            "type": "string"
          },
          "picPhoneNumber": {
            "type": "string"
          }
        }
      },
      "approve201ticket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "ticketId": {
                "type": "string"
              },
              "ticketNossa": {
                "type": "string"
              }
            }
          }
        }
      },
      "bodyReject": {
        "type": "object",
        "properties": {
          "ticketId": {
            "type": "string"
          },
          "reason": {
            "type": "string"
          },
          "attachment": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "image": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "reject201ticket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "ticketId": {
                "type": "string"
              }
            }
          }
        }
      },
      "400": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object"
          }
        }
      },
      "search200ticket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "ticketId": {
                  "type": "string"
                },
                "id": {
                  "type": "string"
                },
                "category": {
                  "type": "string"
                },
                "corporateClientName": {
                  "type": "string"
                },
                "serviceName": {
                  "type": "string"
                },
                "location": {
                  "type": "string"
                },
                "complaint": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "createdAt": {
                  "type": "string"
                },
                "rating": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "integer"
                    },
                    "dateTime": {
                      "type": "string"
                    },
                    "message": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer"
              },
              "size": {
                "type": "integer"
              },
              "totalPage": {
                "type": "integer"
              },
              "totalData": {
                "type": "integer"
              }
            }
          }
        }
      },
      "postUploadFile": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "fileName": {
                "type": "string"
              },
              "fileUrl": {
                "type": "string"
              }
            }
          }
        }
      },
      "deleteFile": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          },
          "data": {
            "type": "object"
          }
        }
      },
      "slgPeriode": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataPeriode"
            },
            "example": [
              {
                "id": 201806,
                "label": "SLG Juni 2018"
              },
              {
                "id": 201805,
                "label": "SLG Mei 2018"
              },
              {
                "id": 201804,
                "label": "SLG April 2018"
              },
              {
                "id": 201803,
                "label": "SLG Maret 2018"
              },
              {
                "id": 201802,
                "label": "SLG Februari 2018"
              },
              {
                "id": 201801,
                "label": "SLG Januari 2018"
              }
            ]
          }
        }
      },
      "DataPeriode": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "label": {
            "type": "string"
          }
        }
      },
      "ListSlgPerPeriode": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ListSlg1"
            },
            "example": [
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0028842416",
                "serviceName": "Telkom VPN IP",
                "location": "BANDARA HUSEINSASTRANEGARABANDARA HUSEIN",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0029371753",
                "serviceName": "Telkom VPN IP",
                "location": "APS u/ Starbucks",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0029408101",
                "serviceName": "Telkom VPN IP",
                "location": "T3 BANDARA SOEKARNO HATTA",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0029458919",
                "serviceName": "Telkom VPN IP",
                "location": "Siborong borong Silangit AP",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": 412538906,
                "serviceName": "PINS Device Services",
                "location": "CARGO AREA TANGERANG",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "300106206-0022485998",
                "serviceName": "Telkom ASTINET",
                "location": "JL BASUKI RAHMAT KM 8 SORONG",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0021456765",
                "serviceName": "Telkom ASTINET",
                "location": "Gapura Angkasa, Cargo Area Gd.511",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0021526574",
                "serviceName": "Telkom VPN IP",
                "location": "(PDG-OPS) Padang - Bandara Minangkabau",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4702523-0030520768",
                "serviceName": "TELKOM Metro",
                "location": "Lintasarta u/ Bollore Logistics Indonesia",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "availabilitySlg": "100%",
                "sid": "4702523-0030522594",
                "serviceName": "TELKOM Metro",
                "location": "Lintasarta U/ Bollore Logistics Indonesia",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 10
              },
              "totalPage": {
                "type": "integer",
                "example": 26
              },
              "totalData": {
                "type": "integer",
                "example": 258
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          }
        }
      },
      "ListSlg1": {
        "type": "object",
        "properties": {
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ListSlg2"
            }
          }
        }
      },
      "ListSlg2": {
        "type": "object",
        "properties": {
          "availabilitySlg": {
            "type": "string"
          },
          "sid": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "valueSlg": {
            "type": "string"
          },
          "availableTime": {
            "type": "string"
          }
        }
      },
      "DetailSlg": {
        "type": "object",
        "properties": {
          "success": {
            "type": "string",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "object",
            "properties": {
              "availabilitySlg": {
                "type": "string",
                "example": "99.73%"
              },
              "sid": {
                "type": "string",
                "example": "4709630-1900"
              },
              "serviceName": {
                "type": "string",
                "example": "VPN ID 10 Mbps"
              },
              "location": {
                "type": "string",
                "example": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              },
              "valueSlg": {
                "type": "string",
                "example": "99.5%"
              },
              "availableTime": {
                "type": "number",
                "format": "float",
                "example": 718.056
              },
              "tickets": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Tickets"
                },
                "example": [
                  {
                    "ticketId": 18013813,
                    "ttr": 0.48,
                    "createdAt": "13/10/2018 - 20:08",
                    "complaint": "Astinet tidak stabil"
                  }
                ]
              }
            }
          }
        }
      },
      "DownloadSlg": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "url": {
                "type": "string",
                "example": "https://tds-customer-storage.apps.playcourt.id/tdscustomer/slg-5586820/SLG-201812.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=iud3oCpWeT84nA7hFegN%2F20190415%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190415T032237Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=d14256d1d4ee3af630c429a1fe2c8f0bc71fb4d178a8cdacfe1e1b3eb10bc1c6\""
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          }
        }
      },
      "Tickets": {
        "properties": {
          "ticketId": {
            "type": "integer"
          },
          "TTR": {
            "type": "number",
            "format": "float"
          },
          "createdAt": {
            "type": "string",
            "format": "date-time"
          },
          "complaint": {
            "type": "string"
          }
        }
      },
      "ListMrtg": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ListMrtgs"
            },
            "example": [
              {
                "sid": "4709630-1973",
                "serviceName": "VPN ID 10 Mbps",
                "location": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              },
              {
                "sid": "4709630-1974",
                "serviceName": "VPN ID 10 Mbps",
                "location": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              },
              {
                "sid": "4709630-1975",
                "serviceName": "VPN ID 10 Mbps",
                "location": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              },
              {
                "sid": "4709630-1976",
                "serviceName": "VPN ID 10 Mbps",
                "location": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              }
            ]
          }
        }
      },
      "ListMrtgs": {
        "properties": {
          "sid": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "location": {
            "type": "string"
          }
        }
      },
      "DataMrtg": {
        "properties": {
          "sid": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "location": {
            "type": "string"
          }
        }
      },
      "DataSlg": {
        "properties": {
          "availabilitySlg": {
            "type": "string"
          },
          "sid": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "valueSlg": {
            "type": "string"
          },
          "availableTime": {
            "type": "string"
          }
        }
      },
      "DetailMrtg": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "object",
            "properties": {
              "requestMrtg": {
                "type": "object",
                "properties": {
                  "status": {
                    "type": "boolean",
                    "example": true
                  },
                  "dateTime": {
                    "type": "string",
                    "example": "13/10/2019-11:30"
                  }
                }
              },
              "sid": {
                "type": "string",
                "example": "4709630-1973"
              },
              "serviceName": {
                "type": "string",
                "example": "VPN ID 10 Mbps"
              },
              "location": {
                "type": "string",
                "example": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              },
              "mrtgReport": {
                "type": "string",
                "example": ""
              }
            }
          }
        }
      },
      "SearchMrtg": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataMrtg"
            },
            "example": [
              {
                "sid": 1279358,
                "serviceName": "Manage Network",
                "location": "Ds. KARANGREJA PURBOLINGGO JAWA TENGAH,-,Purbolinggo,99999"
              },
              {
                "sid": "04702581",
                "serviceName": "Manage Network",
                "location": "Ds. SUKABUMI KEC. CEPOGO  BOYOLALI  JAWA TENGAH,-,Boyolali,99999"
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 2
              },
              "totalPage": {
                "type": "integer",
                "example": 138
              },
              "totalData": {
                "type": "integer",
                "example": 275
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          }
        }
      },
      "SearchSlg": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataSlg"
            },
            "example": [
              {
                "availabilitySlg": "100%",
                "sid": "4703277-0005991483",
                "serviceName": "Telkom VPN IP",
                "location": "Ds. KARANGREJA PURBOLINGGO JAWA TENGAH,-,Purbolinggo,99999",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              },
              {
                "sid": "04702581",
                "serviceName": "Manage Network",
                "location": "Ds. SUKABUMI KEC. CEPOGO  BOYOLALI  JAWA TENGAH,-,Boyolali,99999",
                "valueSlg": "99%",
                "availableTime": "744 jam"
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 1
              },
              "size": {
                "type": "integer",
                "example": 2
              },
              "totalPage": {
                "type": "integer",
                "example": 138
              },
              "totalData": {
                "type": "integer",
                "example": 275
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          }
        }
      },
      "MrtgRequest": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "object",
            "properties": {
              "requestId": {
                "type": "string",
                "example": "8c091162-8058-46fa-a2d1-89e23e0b9c9c"
              },
              "createdBy": {
                "type": "string",
                "example": 940038
              },
              "sid": {
                "type": "string",
                "example": "4700074-0020724486"
              },
              "serviceName": {
                "type": "string",
                "example": "MPLS VPN IP Network"
              },
              "location": {
                "type": "string",
                "example": "Jl Residen Danubroto No 6 Geuceu Komplek,-,Banda Aceh,99999"
              },
              "createdAt": {
                "type": "string",
                "example": "2019-06-12 08:56:45 UTC"
              }
            }
          }
        }
      },
      "detailTicketAM": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "tdsTicketId": {
                "type": "string",
                "example": "TDS-3001068401-00309614591555051969568"
              },
              "ticketId": {
                "type": "string",
                "example": "IN123459"
              },
              "sid": {
                "type": "string",
                "example": "4709630-1973"
              },
              "custAccntName": {
                "type": "string",
                "example": "TELKOMSEL"
              },
              "categoryName": {
                "type": "string",
                "example": "E001"
              },
              "serviceName": {
                "type": "string",
                "example": "Astinet 100M"
              },
              "location": {
                "type": "string",
                "example": "Jln Cihanjuang, Cimahi, Jawa Barat"
              },
              "complaint": {
                "type": "string",
                "example": "Tidak bisa internetan padahal semua led di STB sudah oke"
              },
              "status": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/ListStatus"
                },
                "example": [
                  {
                    "status": "Tiket Terbit",
                    "dateTime": "2019-02-12 10:31:46 UTC"
                  },
                  {
                    "status": "Penanganan",
                    "dateTime": "2019-02-12 10:34:26 UTC",
                    "detail": [
                      {
                        "step": 1,
                        "status": "Analisa Ticket",
                        "note": null,
                        "dateTime": null
                      },
                      {
                        "step": 2,
                        "status": "Penanganan Teknis",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T14:45:05.699Z",
                        "createdBy": ""
                      },
                      {
                        "step": 3,
                        "status": "Penyelesaian Teknis",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      }
                    ]
                  },
                  {
                    "status": "Selesai",
                    "dateTime": "2019-02-12 10:34:26 UTC"
                  }
                ]
              },
              "statusTicket": {
                "type": "string",
                "example": "Selesai"
              },
              "createdAt": {
                "type": "string",
                "example": "2019-02-06T04:40:55.190Z"
              },
              "updatedAt": {
                "type": "string",
                "example": "2019-02-12T10:53:47.669Z"
              },
              "rating": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "integer",
                    "example": 5
                  },
                  "dateTime": {
                    "type": "string",
                    "example": "2019-02-06T04:40:55.190Z"
                  },
                  "message": {
                    "type": "string",
                    "example": "Tes"
                  }
                }
              },
              "node": {
                "type": "string",
                "example": "PE-D3-LBG-VPN"
              },
              "interfaces": {
                "type": "string",
                "example": "Gi0/7/0/10.3610"
              },
              "description": {
                "type": "string",
                "example": "470089-0029677009 VPN IP KIMIA FARMA Jl Cihampelas No 5 Bandung"
              },
              "picName": {
                "type": "string",
                "example": "Novi"
              },
              "picPhoneNumber": {
                "type": "string",
                "example": "082326066070"
              }
            }
          },
          "message": {
            "type": "string",
            "example": "Here are the detail for undefined"
          },
          "code": {
            "type": "string",
            "example": 200
          }
        }
      },
      "ListStatus": {
        "type": "object",
        "properties": {
          "status": {
            "type": "string"
          },
          "statusAlias": {
            "type": "string"
          },
          "dateTime": {
            "type": "string"
          },
          "detail": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DetailStatus"
            }
          },
          "note": {
            "type": "string"
          }
        }
      },
      "DetailStatus": {
        "type": "object",
        "properties": {
          "step": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "statusAlias": {
            "type": "string"
          },
          "dateTime": {
            "type": "string"
          },
          "note": {
            "type": "string"
          },
          "createdBy": {
            "type": "string"
          }
        }
      },
      "detailTicketEOSAM": {
        "type": "object",
        "oneOf": [
          {
            "$ref": "#/components/schemas/detailTicketEOS"
          },
          {
            "$ref": "#/components/schemas/detailTicketAM"
          },
          {
            "$ref": "#/components/schemas/rejectTicket"
          }
        ]
      },
      "rejectTicket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "tdsTicketId": {
                "type": "string"
              },
              "ticketId": {
                "type": "string"
              },
              "sid": {
                "type": "string"
              },
              "corporateClientName": {
                "type": "string"
              },
              "categoryName": {
                "type": "string"
              },
              "serviceName": {
                "type": "string"
              },
              "location": {
                "type": "string"
              },
              "status": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "statusTicket": {
                "type": "string"
              },
              "createdAt": {
                "type": "string"
              },
              "updatedAt": {
                "type": "string"
              },
              "picName": {
                "type": "string"
              },
              "picPhoneNumber": {
                "type": "string"
              },
              "channel": {
                "type": "string"
              },
              "reason": {
                "type": "string"
              },
              "attachment": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "image": {
                      "type": "string"
                    },
                    "fileName": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "detailTicketEOS": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "tdsTicketId": {
                "type": "string",
                "example": "TDS-3001068401-00309614591555051969568"
              },
              "ticketId": {
                "type": "string",
                "example": "IN123459"
              },
              "sid": {
                "type": "string",
                "example": "4709630-1973"
              },
              "custAccntName": {
                "type": "string",
                "example": "TELKOMSEL"
              },
              "categoryName": {
                "type": "string",
                "example": "E001"
              },
              "serviceName": {
                "type": "string",
                "example": "Astinet 100M"
              },
              "location": {
                "type": "string",
                "example": "Jln Cihanjuang, Cimahi, Jawa Barat"
              },
              "complaint": {
                "type": "string",
                "example": "Tidak bisa internetan padahal semua led di STB sudah oke"
              },
              "status": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/ListStatus"
                },
                "example": [
                  {
                    "status": "Tiket Terbit",
                    "dateTime": "2019-02-12 10:31:46 UTC"
                  },
                  {
                    "status": "Penanganan",
                    "dateTime": "2019-02-12 10:34:26 UTC",
                    "detail": [
                      {
                        "step": 1,
                        "status": "Send to Tier 2",
                        "statusAlias": "Analisa Teknis",
                        "note": null,
                        "dateTime": null,
                        "createdby": "NOSSA"
                      },
                      {
                        "step": 2,
                        "status": "NetCool Wait for Impacted Services",
                        "statusAlias": "Analisa Teknis",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T14:45:05.699Z",
                        "createdBy": ""
                      },
                      {
                        "step": 3,
                        "status": "Pending-SLA Hold",
                        "statusAlias": "Penanganan Tertunda",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      },
                      {
                        "step": 4,
                        "status": "Send to Tier 3",
                        "statusAlias": "Penanganan Teknis",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      },
                      {
                        "step": 5,
                        "status": "Final Check",
                        "statusAlias": "Penyelesaian Masalah",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      },
                      {
                        "step": 6,
                        "status": "Resolved (Technical Closed)",
                        "statusAlias": "Penyelesaian Masalah",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      },
                      {
                        "step": 7,
                        "status": "Media Caring",
                        "statusAlias": "Penyelesaian Masalah",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      },
                      {
                        "step": 8,
                        "status": "Salam Simpatik",
                        "statusAlias": "Penyelesaian Masalah",
                        "note": "VPN IP Mati Total Logic",
                        "dateTime": "2019-04-12T07:16:04.422Z",
                        "createdBy": ""
                      }
                    ]
                  },
                  {
                    "status": "Closed",
                    "statusAlias": "Selesai",
                    "dateTime": "2019-02-12 10:34:26 UTC"
                  }
                ]
              },
              "statusTicket": {
                "type": "string",
                "example": "Selesai"
              },
              "createdAt": {
                "type": "string",
                "example": "2019-02-06T04:40:55.190Z"
              },
              "updatedAt": {
                "type": "string",
                "example": "2019-02-12T10:53:47.669Z"
              },
              "rating": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": "integer",
                    "example": 5
                  },
                  "dateTime": {
                    "type": "string",
                    "example": "2019-02-06T04:40:55.190Z"
                  },
                  "message": {
                    "type": "string",
                    "example": "Tes"
                  }
                }
              },
              "node": {
                "type": "string",
                "example": "PE-D3-LBG-VPN"
              },
              "interfaces": {
                "type": "string",
                "example": "Gi0/7/0/10.3610"
              },
              "description": {
                "type": "string",
                "example": "470089-0029677009 VPN IP KIMIA FARMA Jl Cihampelas No 5 Bandung"
              },
              "picName": {
                "type": "string",
                "example": "Novi"
              },
              "picPhoneNumber": {
                "type": "string",
                "example": "082326066070"
              }
            }
          },
          "message": {
            "type": "string",
            "example": "Here are the detail for undefined"
          },
          "code": {
            "type": "string",
            "example": 200
          }
        }
      },
      "Services": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ListServices"
            },
            "example": [
              {
                "id": "A_INTERNET",
                "parent": "ROOT",
                "name": "INTERNET"
              }
            ]
          }
        }
      },
      "Symptom": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ListSymptom"
            },
            "example": [
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_001 \\ A_INTERNET_001_001_001",
                "symptomname": "Tidak Bisa Browsing - Tidak Bisa Koneksi"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_001 \\ A_INTERNET_001_001_002",
                "symptomname": "Tidak Bisa Browsing - 2P / 3P Mati Total"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_001 \\ A_INTERNET_001_001_003",
                "symptomname": "Tidak Bisa Browsing - Gangguan Pasca PSB < 30Hr"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_001",
                "symptomname": "Bisa Browsing - Tidak Bisa Email"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_002",
                "symptomname": "Bisa Browsing - Tidak Bisa ke Website Tertentu"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_003",
                "symptomname": "Bisa Browsing - Lambat"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_004",
                "symptomname": "Bisa Browsing - Intermitten / Putus-Putus"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_005",
                "symptomname": "Bisa Browsing - Gangguan Game Online"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_006",
                "symptomname": "Bisa Browsing - Gangguan IP Publik"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_002 \\ A_INTERNET_001_002_007",
                "symptomname": "Bisa Browsing - Push Advertising"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_003 \\ A_INTERNET_001_003_001",
                "symptomname": "Perangkat Pelanggan - Sharing Koneksi LAN/WiFi"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_003 \\ A_INTERNET_001_003_002",
                "symptomname": "Perangkat Pelanggan - Petugas Diminta Datang"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_003 \\ A_INTERNET_001_003_003",
                "symptomname": "modem rusak"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_004 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_005 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_001_006 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_002_001 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_002_002 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_002_003 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_002_004 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_001 \\ A_INTERNET_002_005 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_006 \\ A_INTERNET_002_006_001",
                "symptomname": "Registrasi TSI-9 (Indihome)"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_006 \\ A_INTERNET_002_006_002",
                "symptomname": "Registrasi TSI-3 (Non Indihome)"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_006 \\ A_INTERNET_002_006_003",
                "symptomname": "Registrasi TSI-7 (Coorporate/DES)"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_007 \\ A_INTERNET_002_007_001",
                "symptomname": "UnReg TSI-9 (Indihome)"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_007 \\ A_INTERNET_002_007_002",
                "symptomname": "UnReg TSI-3 (Non Indihome)"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_007 \\ A_INTERNET_002_007_003",
                "symptomname": "UnReg TSI-7 (Coorporate/DES)"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_008 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_009 \\",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_010",
                "symptomname": ""
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_011 \\ A_INTERNET_002_011_001",
                "symptomname": "Tidak bisa Bayar - Error Moda Bayar"
              },
              {
                "symptomcode": "A_INTERNET \\ A_INTERNET_002 \\ A_INTERNET_002_011 \\ A_INTERNET_002_011_002",
                "symptomname": "Tidak bisa Bayar - Error Data Komersial"
              }
            ]
          }
        }
      },
      "ListSymptom": {
        "type": "object",
        "properties": {
          "symptomcode": {
            "type": "string"
          },
          "symptomname": {
            "type": "string"
          }
        }
      },
      "ListServices": {
        "properties": {
          "id": {
            "type": "string"
          },
          "parent": {
            "type": "string"
          },
          "name": {
            "type": "string"
          }
        }
      },
      "SuggestSID": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SidSuggestion"
            },
            "example": [
              {
                "sid": "4700012-0001557231"
              },
              {
                "sid": "4700012-0001561863"
              }
            ]
          }
        }
      },
      "SearchSID": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/SidData"
            },
            "example": [
              {
                "sid": "4700074-0020724486",
                "location": "Jl Residen Danubroto No 6 Geuceu Komplek,-,Banda Aceh,99999",
                "serviceId": "VPNIP_NODE",
                "serviceName": "MPLS VPN IP Network"
              },
              {
                "sid": "4700074-0020724486",
                "location": "Jl Residen Danubroto No 6 Geuceu Komplek,-,Banda Aceh,99999",
                "serviceId": "VPNIP_NODE",
                "serviceName": "MPLS VPN IP Node"
              }
            ]
          }
        }
      },
      "salist200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              {
                "rowId": "1-A1M-1276",
                "serviceAccountName": "BANK MANDIRI KANTOR CABANG PURWOKERTO",
                "location": "JL. JEND SOEDIRMAN,-7.427075853542199,TENOSS,PURWOKERTO,99999"
              }
            ]
          }
        }
      },
      "serviceList200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              {
                "sid": "4700037-97456",
                "serviceName": "MPLS VPN IP Network",
                "serviceId": "VPNIP_NETWORK",
                "category": "Data & Internet Products",
                "netType": "Network",
                "status": "Active"
              }
            ]
          }
        }
      },
      "DetailSID": {
        "type": "object",
        "properties": {
          "success": {
            "type": "string",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "object",
            "properties": {
              "categoryId": {
                "type": "string",
                "example": "001"
              },
              "categoryName": {
                "type": "string",
                "example": "Connectivity"
              },
              "sid": {
                "type": "string",
                "example": "4709630-1974"
              },
              "location": {
                "type": "string",
                "example": "Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10110."
              },
              "serviceId": {
                "type": "string",
                "example": ""
              },
              "serviceName": {
                "type": "string",
                "example": "VPN ID 10 Mbps"
              },
              "symptoms": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/SymtompDetail"
                },
                "example": [
                  {
                    "symptomId": "A_INTERNET \\\\ A_INTERNET_001 \\\\ A_INTERNET_001_001 \\\\ A_INTERNET_001_001_001",
                    "symptomDescription": "Tidak Bisa Browsing - Tidak Bisa Koneksi"
                  }
                ]
              },
              "node": {
                "type": "string",
                "example": "01MyTDS"
              },
              "interface": {
                "type": "string",
                "example": "MyTDS2020"
              },
              "description": {
                "type": "string",
                "example": "4709630-1974 VPN ID 10 Mbps Jl. Kebon Sirih No.12, RT.11/RW.2, Gambir"
              }
            }
          }
        }
      },
      "SymtompDetail": {
        "type": "object",
        "properties": {
          "symptomId": {
            "type": "string"
          },
          "symptomName": {
            "type": "string"
          }
        }
      },
      "SidSuggestion": {
        "type": "object",
        "properties": {
          "sid": {
            "type": "string"
          }
        }
      },
      "SidData": {
        "type": "object",
        "properties": {
          "sid": {
            "type": "string"
          },
          "location": {
            "type": "string"
          },
          "serviceId": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          }
        }
      },
      "allNotifResp": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "notificationId": {
                  "type": "string"
                },
                "date": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "custAccntNum": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "message": {
                  "type": "string"
                },
                "data": {
                  "type": "object",
                  "properties": {
                    "productId": {
                      "type": "string"
                    },
                    "marketableTitle": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    },
                    "date": {
                      "type": "string"
                    }
                  }
                },
                "isRead": {
                  "type": "boolean"
                }
              }
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer"
              },
              "size": {
                "type": "integer"
              },
              "totalPage": {
                "type": "integer"
              },
              "totalData": {
                "type": "integer"
              }
            }
          }
        }
      },
      "detailIfrs200": {
        "type": "object",
        "properties": {
          "agreeName": {
            "type": "string"
          },
          "agreeNum": {
            "type": "string"
          },
          "corporateClientName": {
            "type": "string"
          },
          "startDate": {
            "type": "string"
          },
          "endDate": {
            "type": "string"
          },
          "serviceCount": {
            "type": "integer"
          },
          "contractValue": {
            "type": "integer"
          },
          "docUrl": {
            "type": "string"
          },
          "docName": {
            "type": "string"
          },
          "fileType": {
            "type": "string"
          },
          "serviceName": {
            "type": "string"
          },
          "servicePoint": {
            "type": "integer"
          },
          "serviceValue": {
            "type": "integer"
          }
        }
      },
      "ifrsFilter": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string"
              },
              "detail": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "title": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "NotifList": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/NotifData"
            },
            "example": [
              {
                "notificationId": "3b4b4c91-c05f-42e7-9c15-a6c7017499cb",
                "date": "2019-05-06T02:33:54.640Z",
                "type": "ifrs",
                "nipnas": 2914219,
                "title": "Penyediaan layanan telkom solution",
                "message": "Kontrak Anda akan berakhir dalam 1 Hari lagi dan Anda belum melakukan konfirmasi untuk perpanjangan kontrak dengan detail berikut.",
                "data": {
                  "ifrsId": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae",
                  "contractTitle": "Penyediaan layanan telkom solution",
                  "contractNumber": "k.tel./hk.811/des-mcs/2019",
                  "corporateClientName": "TELKOMSEL",
                  "contractFile": ""
                },
                "isRead": false
              },
              {
                "notificationId": "3fe7bb44-aa40-4a4c-abe0-7b6103045fff",
                "date": "2019-05-07T06:24:54.983Z",
                "type": "ticket",
                "nipnas": 2000259,
                "title": "Ticket Telah Terbit",
                "message": "Kepada Pelanggan, tiket gangguan Anda telah terbit dengan no TestQA001.",
                "data": {
                  "tdsTicketId": "NS010002",
                  "tdsTicketNossa": "IN123",
                  "serviceName": "MPLS VPN IP Node",
                  "serviceLocation": "ASTRA SEDAYA FINANCE PADANG Jl.Khatib Sulaiman,PDULK,Padang - Sumatra Bar,99999",
                  "detailText": "LIHAT DETAIL TICKET GANGGUAN",
                  "custAccntName": "ASTRA SEDAYA FINANCE PT",
                  "serviceId": "SID 4700167-24706"
                },
                "isRead": false
              },
              {
                "notificationId": "e824cb76-0d3b-4236-96d2-a1e69d4a63aa",
                "date": {
                },
                "type": "ticket",
                "nipnas": 2914219,
                "title": "Tiket Terbit",
                "message": "Kepada Pelanggan, tiket gangguan Anda telah terbit dengan no TestQA002.",
                "data": {
                  "tdsTicketId": "TDS-3001068401",
                  "tdsTicketNossa": "TestQA001",
                  "serviceName": "Metro Link",
                  "serviceLocation": "Jl. Kebon Sirih I, DKI Jakarta",
                  "detailText": "LIHAT DETAIL TICKET GANGGUAN",
                  "custAccntName": "ASTRA SEDAYA FINANCE PT",
                  "serviceId": "SID 4700167-24734"
                },
                "isRead": true
              }
            ]
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer",
                "example": 2
              },
              "size": {
                "type": "integer",
                "example": 3
              },
              "totalPage": {
                "type": "integer",
                "example": 2
              },
              "totalData": {
                "type": "integer",
                "example": 4
              }
            }
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success get list notification"
          }
        }
      },
      "NotifData": {
        "type": "object",
        "properties": {
          "notificationId": {
            "type": "string"
          },
          "date": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "nipnas": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object"
          },
          "isRead": {
            "type": "boolean"
          }
        }
      },
      "NotifCount": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "data": {
            "type": "object",
            "properties": {
              "count": {
                "type": "integer",
                "example": 3
              }
            }
          },
          "message": {
            "type": "string",
            "example": "Success get count notification"
          },
          "code": {
            "type": "string",
            "example": 200
          }
        }
      },
      "IsRead": {
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "string",
            "example": "OK"
          }
        }
      },
      "bodyHelpdesk": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "example": "Novi Arliani"
          },
          "email": {
            "type": "string",
            "example": "noviarliani@gmail.com"
          },
          "issueDesc": {
            "type": "string",
            "example": "Reset Password"
          },
          "issueDetail": {
            "type": "string",
            "example": "Saya ingin melakukan reset password"
          },
          "image": {
            "type": "string",
            "example": "https://tds-customer-storage.apps.playcourt.id/tdscustomerpublic/tds-cc-default-profile-pict.png"
          }
        }
      },
      "helpdesk200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "NotifTicket": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "ticket"
          },
          "custAccntNum": {
            "type": "string",
            "example": 1280502
          },
          "title": {
            "type": "string",
            "example": "Tiket Terbit"
          },
          "message": {
            "type": "string",
            "example": "Kepada Pelanggan, tiket gangguan Anda telah terbit dengan no TestQA002."
          },
          "data": {
            "type": "object",
            "properties": {
              "tdsTicketId": {
                "type": "string",
                "example": "TDS-3001068401"
              },
              "tdsTicketNossa": {
                "type": "string",
                "example": "TestQA001"
              },
              "serviceName": {
                "type": "string",
                "example": "Metro Link"
              },
              "serviceLocation": {
                "type": "string",
                "example": "Jl. Kebon Sirih I, DKI Jakarta"
              },
              "detailText": {
                "type": "string",
                "example": "LIHAT DETAIL TICKET GANGGUAN"
              }
            }
          }
        }
      },
      "NotifIfrs": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "ifrs"
          },
          "custAccntNum": {
            "type": "string",
            "example": 1280502
          },
          "title": {
            "type": "string",
            "example": "Penyediaan layanan telkom solution"
          },
          "message": {
            "type": "string",
            "example": "Kontrak Anda akan berakhir dalam 1 Hari lagi dan Anda belum melakukan konfirmasi untuk perpanjangan kontrak dengan detail berikut."
          },
          "data": {
            "type": "object",
            "properties": {
              "ifrsId": {
                "type": "string",
                "example": "ef5902f9-ca7b-4ec0-9c7b-3e437d0dccae"
              },
              "contractTitle": {
                "type": "string",
                "example": "Penyediaan layanan telkom solution"
              },
              "contractNumber": {
                "type": "string",
                "example": "k.tel./hk.811/des-mcs/2019"
              },
              "corporateClientName": {
                "type": "string",
                "example": "TELKOMSEL"
              },
              "contractFile": {
                "type": "string",
                "example": ""
              }
            }
          }
        }
      },
      "200NotifTicket": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Create Notification success"
          },
          "data": {
            "type": "string",
            "example": "OK"
          }
        }
      },
      "200NotifIfrs": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Create Notification success"
          },
          "data": {
            "type": "string",
            "example": "OK"
          }
        }
      },
      "NOK": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "data": {
            "type": "string",
            "example": ""
          },
          "message": {
            "type": "string",
            "example": "SID Sudah Di laporkan Gangguan"
          },
          "code": {
            "type": "string",
            "example": 500
          }
        }
      },
      "NOK1": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "message": {
            "type": "string",
            "example": "that is not your NIK"
          },
          "code": {
            "type": "string",
            "example": 400
          },
          "data": {
            "type": "string",
            "example": ""
          }
        }
      },
      "401tokenInvalid": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "data": {
            "type": "object"
          },
          "message": {
            "type": "string"
          },
          "code": {
            "type": "string"
          }
        }
      },
      "NOK3": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "data": {
            "type": "string",
            "example": ""
          },
          "message": {
            "type": "string",
            "example": "Cannot get list Data. System Fault"
          },
          "code": {
            "type": "string",
            "example": 500
          }
        }
      },
      "NOK4": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "data": {
            "type": "string",
            "example": ""
          },
          "message": {
            "type": "string",
            "example": "that is not your NIK"
          },
          "code": {
            "type": "string",
            "example": 400
          }
        }
      },
      "nok404": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": false
          },
          "data": {
            "type": "string",
            "example": ""
          },
          "message": {
            "type": "string",
            "example": "Data not found"
          },
          "code": {
            "type": "integer",
            "example": 404
          }
        }
      },
      "faqLogin200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/faqLoginType"
            },
            "example": [
              {
                "header": "Cara masuk ke akun MyTDS AM",
                "body": "Untuk masuk ke aplikasi MyTDS AM, ikuti langkah mudah berikut",
                "point": [
                  {
                    "row": "1. Buka aplikasi MyTDS AM."
                  },
                  {
                    "row": "2. Jika kamu seorang AM, masukkan NIK dan Password Portal Telkom kamu.\\n      Sedangkan jika kamu seorang EOS, masukkan NIK kamu dan password yang telah diberikan."
                  },
                  {
                    "row": "3. Selamat! Kamu sudah berhasil masuk ke akun MyTDS AM."
                  }
                ]
              }
            ]
          }
        }
      },
      "faqLoginType": {
        "type": "object",
        "properties": {
          "header": {
            "type": "string"
          },
          "body": {
            "type": "string"
          },
          "point": {
            "type": "object",
            "properties": {
              "row": {
                "type": "string"
              }
            }
          }
        }
      },
      "issueCategory200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/issueCategoryType"
            },
            "example": [
              {
                "issueId": "I001",
                "issueDesc": "Umum"
              },
              {
                "issueId": "I002",
                "issueDesc": "Reset Password"
              }
            ]
          }
        }
      },
      "issueCategoryType": {
        "type": "object",
        "properties": {
          "issueId": {
            "type": "string"
          },
          "issueDesc": {
            "type": "string"
          }
        }
      },
      "callEOS": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "integer",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Your Request Has Been Processed"
          },
          "data": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataCallEos"
            },
            "example": [
              {
                "eosId": 30959,
                "eosName": "AHMAD DAURI",
                "eosPhoneNumber": "082232767523"
              },
              {
                "eosId": 30959,
                "eosName": "AHMAD DAURI",
                "eosPhoneNumber": "082232767523"
              }
            ]
          }
        }
      },
      "DataCallEos": {
        "type": "object",
        "properties": {
          "eosId": {
            "type": "integer"
          },
          "eosName": {
            "type": "string"
          },
          "eosPhoneNumber": {
            "type": "string"
          }
        }
      },
      "bodyLogstashHelpdesk": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "example": "Whatsapp"
          }
        }
      },
      "helpdeskAnalytic200": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "feedback200user": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "properties": {
              "rating": {
                "type": "integer",
                "example": 4
              },
              "detail": {
                "type": "string",
                "example": "Mantap"
              },
              "createdAt": {
                "type": "string",
                "example": "2020-01-27T07:33:22.364Z"
              }
            }
          }
        }
      },
      "bodyRating": {
        "type": "object",
        "properties": {
          "rating": {
            "type": "integer",
            "example": 4
          },
          "detail": {
            "type": "string",
            "example": "Mantap"
          }
        }
      },
      "feedback200body": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "helpdesk200contact": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 200
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "properties": {
              "wa": {
                "type": "string",
                "example": "082147493994"
              },
              "telephone": {
                "type": "string",
                "example": "082147493994"
              },
              "chataja": {
                "type": "string",
                "example": "082147493994"
              }
            }
          }
        }
      },
      "notif200doc": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string"
              },
              "header": {
                "type": "string"
              },
              "point": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "row": {
                      "type": "string"
                    }
                  }
                }
              },
              "footer": {
                "type": "string"
              }
            }
          }
        }
      },
      "list200docs": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "agreeName": {
                  "type": "string"
                },
                "agreeNum": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "endContract": {
                  "type": "string"
                },
                "contractValue": {
                  "type": "integer"
                }
              }
            }
          },
          "meta": {
            "type": "object",
            "properties": {
              "page": {
                "type": "integer"
              },
              "size": {
                "type": "integer"
              },
              "totalData": {
                "type": "integer"
              },
              "totalPage": {
                "type": "integer"
              }
            }
          }
        }
      },
      "profileBody": {
        "type": "object",
        "properties": {
          "userId": {
            "type": "string",
            "example": "123qwe"
          },
          "phone": {
            "type": "string",
            "example": "082326066070"
          },
          "email": {
            "type": "string",
            "example": "noviarliani@gmail.com"
          },
          "address": {
            "type": "string",
            "example": "Kos Meryl 65, Jl. Kramat II"
          }
        }
      },
      "profile200get": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "_id": {
                "type": "string"
              },
              "nik": {
                "type": "string"
              },
              "userId": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "password": {
                "type": "string"
              },
              "salt": {
                "type": "string"
              },
              "applicationType": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "createdAt": {
                "type": "string"
              },
              "updatedAt": {
                "type": "string"
              },
              "createdBy": {
                "type": "string"
              },
              "updatedBy": {
                "type": "string"
              },
              "needApproval": {
                "type": "boolean"
              },
              "isActive": {
                "type": "boolean"
              },
              "metaData": {
                "type": "object",
                "properties": {
                  "nik": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "fullName": {
                    "type": "string"
                  },
                  "location": {
                    "type": "string"
                  },
                  "phoneNumber": {
                    "type": "string"
                  },
                  "company": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "category": {
                        "type": "string"
                      },
                      "subCategory": {
                        "type": "string"
                      }
                    }
                  },
                  "ccHandled": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "nipnas": {
                          "type": "integer"
                        },
                        "corporateClientName": {
                          "type": "string"
                        },
                        "segment": {
                          "type": "string"
                        },
                        "location": {
                          "type": "string"
                        },
                        "witel": {
                          "type": "string"
                        },
                        "divre": {
                          "type": "string"
                        },
                        "startHandled": {
                          "type": "string"
                        },
                        "endHandled": {
                          "type": "string"
                        },
                        "ccRemote": {
                          "type": "string"
                        },
                        "custAccntNum": {
                          "type": "string"
                        }
                      }
                    }
                  },
                  "divisionCode": {
                    "type": "string"
                  },
                  "division": {
                    "type": "string"
                  },
                  "unit": {
                    "type": "string"
                  },
                  "subUnit": {
                    "type": "string"
                  },
                  "jobTitle": {
                    "type": "string"
                  },
                  "photo": {
                    "type": "string"
                  },
                  "nipnas": {
                    "type": "integer"
                  },
                  "role": {
                    "type": "object",
                    "properties": {
                      "roleId": {
                        "type": "string"
                      },
                      "roleName": {
                        "type": "string"
                      },
                      "roleChilds": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "apps": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "appId": {
                              "type": "string"
                            },
                            "appName": {
                              "type": "string"
                            }
                          }
                        }
                      }
                    }
                  },
                  "segment": {
                    "type": "string"
                  },
                  "customerAccountNumber": {
                    "type": "string"
                  },
                  "firebaseToken": {
                    "type": "string"
                  },
                  "statusInvitation": {
                    "type": "string"
                  },
                  "atasan": {
                    "type": "object",
                    "properties": {
                      "nik": {
                        "type": "string"
                      },
                      "nama": {
                        "type": "string"
                      },
                      "posisi": {
                        "type": "string"
                      },
                      "objidposisi": {
                        "type": "string"
                      }
                    }
                  },
                  "nikAm": {
                    "type": "string"
                  },
                  "ratingDate": {
                    "type": "string"
                  },
                  "ratingStatus": {
                    "type": "string"
                  },
                  "lastLogin": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "busUnitDept": {
                    "type": "string"
                  },
                  "lastRefreshToken": {
                    "type": "string"
                  },
                  "nameApp": {
                    "type": "string"
                  },
                  "longUnit": {
                    "type": "string"
                  }
                }
              }
            }
          }
        }
      },
      "profile201update": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 201
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "properties": {
              "phone": {
                "type": "string",
                "example": "082326066070"
              },
              "email": {
                "type": "string",
                "example": "noviarliani@gmail.com"
              },
              "address": {
                "type": "string",
                "example": "Kos Meryl 65, Jl. Kramat II"
              },
              "signatureCode": {
                "type": "string",
                "example": "123nmdenor458"
              }
            }
          }
        }
      },
      "bodyPhoto": {
        "type": "object",
        "properties": {
          "photo": {
            "type": "string"
          }
        }
      },
      "photo200post": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "photo": {
                "type": "string"
              }
            }
          }
        }
      },
      "500": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object"
          }
        }
      },
      "bodyOtp": {
        "type": "object",
        "properties": {
          "phone": {
            "type": "string",
            "example": "082326066070"
          },
          "type": {
            "type": "string",
            "example": "Update Profile"
          },
          "signatureCode": {
            "type": "string",
            "example": "123nmdenor458"
          }
        }
      },
      "otp200post": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 201
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "properties": {
              "signatureCode": {
                "type": "string",
                "example": "123nmdenor458"
              },
              "count": {
                "type": "integer",
                "example": 3
              },
              "expiredAt": {
                "type": "integer",
                "example": 86400
              }
            }
          }
        }
      },
      "bodyOtpVerify": {
        "type": "object",
        "properties": {
          "otp": {
            "type": "string",
            "example": "123myTDS"
          },
          "signatureCode": {
            "type": "string",
            "example": "123nmdenor458"
          }
        }
      },
      "otp200verify": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 201
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "properties": {
              "otp": {
                "type": "string",
                "example": "123myTDS"
              },
              "signatureCode": {
                "type": "string",
                "example": "123nmdenor458"
              }
            }
          }
        }
      },
      "bodyForgotPass": {
        "type": "object",
        "properties": {
          "nik": {
            "type": "string",
            "example": 926015
          }
        }
      },
      "forgot200password": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 201
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "properties": {
              "isLdap": {
                "type": "boolean",
                "example": false
              },
              "signatureCode": {
                "type": "string",
                "example": "123nmdenor458"
              },
              "phone": {
                "type": "string",
                "example": "082326066070"
              }
            }
          }
        }
      },
      "bodyResetPass": {
        "type": "object",
        "properties": {
          "password": {
            "type": "string",
            "example": "123qwe"
          },
          "confirmPass": {
            "type": "string",
            "example": "123qwe"
          },
          "otp": {
            "type": "string",
            "example": "123myTDS"
          },
          "signatureCode": {
            "type": "string",
            "example": "123nmdenor458"
          }
        }
      },
      "reset201password": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean",
            "example": true
          },
          "code": {
            "type": "string",
            "example": 201
          },
          "message": {
            "type": "string",
            "example": "Success"
          },
          "data": {
            "type": "object",
            "example": {
            }
          }
        }
      },
      "bodyChangePass": {
        "type": "object",
        "properties": {
          "password": {
            "type": "string"
          },
          "confirmPass": {
            "type": "string"
          }
        }
      },
      "change201password": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "signatureCode": {
                "type": "string"
              }
            }
          }
        }
      },
      "bodyCheckUser": {
        "type": "object",
        "properties": {
          "nik": {
            "type": "string"
          },
          "password": {
            "type": "string"
          }
        }
      },
      "check200user": {
        "type": "object",
        "properties": {
          "success": {
            "type": "boolean"
          },
          "code": {
            "type": "string"
          },
          "message": {
            "type": "string"
          },
          "data": {
            "type": "object",
            "properties": {
              "isLdap": {
                "type": "boolean"
              },
              "signatureCode": {
                "type": "string"
              },
              "phone": {
                "type": "string"
              }
            }
          }
        }
      }
    }
  }
}
resperr = '{"success": true, "data": "success", "message": "Update product status success", "code": 200};'
path = jsonData['paths']
for key in path: 
    for method in path[key]: 
        for i,valueResponse in path[key][method]['responses'].items(): 
            for v,valueContent in valueResponse['content']['application/json'].items():
                print(v)
                try: 
                    if v=='example':
                        resp = json.loads(valueResponse['content']['application/json']['example'].replace("\'", '"'))
                    elif v=='examples':
                        resp = json.loads(valueResponse['content']['application/json']['examples'])
                        json.loads(response_read.replace("\'", '"'))
                    elif v=='schemas':
                        ax = str(valueResponse['content']['application/json']['schema'])
                        axc = ax.replace("{'$ref': '#/components/schemas/","")
                        acc = axc.replace("'}","")
                        schemas = jsonData['components']['schemas'][acc]['properties']
                        dat = {}
                        for keySchemas,valScehmas in schemas.items():
                            dat.update({keySchemas: valScehmas['example']})
                        resp = dat
                    elif v=='schema':
                        ax = str(valueResponse['content']['application/json']['schema'])
                        axc = ax.replace("{'$ref': '#/components/schemas/","")
                        acc = axc.replace("'}","")
                        schemas = jsonData['components']['schemas'][acc]['properties']
                        dat = {}
                        for keySchemas,valScehmas in schemas.items():
                            dat.update({keySchemas: valScehmas['example']})
                        resp = dat
                        print(resp)
                except:
                    resp = resperr
                data =  '''
                            app.'''+method+'''("'''+key+'''", (req, res) => {
                            let respon = 
                                '''+json.dumps(resp)+'''
                            return res.status(200).json(respon);
                            });
                        '''
                f = open("output.js", "a")
                f.write(data)
                f.close()

                #open and read the file after the appending:
                f = open("output.js", "r")
                # print(f.read())