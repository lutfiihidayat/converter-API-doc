//param example out schame (done)

"requestBody": {
  "description": "update status body/subject email",
  "content": {
    "multipart/form-data": {
      "schema": {
        "type": "object",
        "properties": {
          "evidenceFiles": {
            "type": "string",
            "format": "binary"
          },
          "evidenceToCustomer": {
            "type": "string",
            "example": "tes"
          },
          "status": {
            "type": "string",
            "example": "technical handling"
          }
        }
      }
    },
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/updateStatusBodySubjectEmail"
      },
      "examples": {
        "ticketAnalyze": {
          "summary": "Ticket Analyze",
          "value": {
            "status": "ticket analyze",
            "from": "occ@telkom.co.id",
            "to": "telkomdigitalsolution2019@gmail.com",
            "note": "Tiket Sedang di Tangani"
          }
        },
        "ticketAnalyzeRejected": {
          "summary": "Ticket Analyze Rejected",
          "value": {
            "status": "rejected",
            "rejectReason": "test reject"
          }
        },
        "customerReview": {
          "summary": "Customer Review",
          "value": {
            "status": "customer review",
            "note": null
          }
        },
        "close": {
          "summary": "Close",
          "value": {
            "status": "close"
          }
        },
        "return": {
          "summary": "Return",
          "value": {
            "status": "returned",
            "note": "nothing"
          }
        }
      }
    }
  }
}, //request body jadi null karena memeiliki 2 content multipart dan app/json

"listTicketsInternal": {
  "properties": {
    "success": {
      "type": "boolean",
      "example": true
    },
    "data": {
      "type": "object",
      "example": [
        {
          "custAccNum": 1280510,
          "custAccName": "Jatis",
          "ticketId": "INA-1599099992193",
          "userId": 30000041033661,
          "applicationType": 2,
          "senderTypeName": "UBER",
          "operatorTypeId": 2,
          "categoryId": "E003",
          "category": "LBA Targeted",
          "senderTypeId": "",
          "troubleOccurs": {
            "dateTime": "2020-08-31T02:26:27.372Z",
            "file": {
              "fileName": "GambarBurger.png",
              "fileUrl": "http://minio-assurance-dev.telkomdigitalsolution.co/tdscustomerpublic/attach-lba-assurance/Jatis/GambarBurger.png"
            }
          },
          "worklog": [
            {
              "step": 0,
              "status": "checking",
              "dateTime": "2020-09-03T02:26:32.221Z",
              "note": "Tiket sedang di Analisa",
              "createdBy": "Selita Jaya"
            },
            {
              "step": 1,
              "status": "onprogress",
              "dateTime": "2020-09-11T00:22:47.987Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            },
            {
              "step": 2,
              "status": "customerreview",
              "dateTime": null,
              "note": null,
              "createdBy": null
            },
            {
              "step": 3,
              "status": "completed",
              "dateTime": null,
              "note": null,
              "createdBy": null
            },
            {
              "step": 4,
              "status": "onprogress",
              "dateTime": "2020-09-11T00:16:51.819Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            }
          ],
          "status": "onprogress",
          "description": "Test Description",
          "picName": "Tes Automation",
          "picPhoneNumber": "081233785197",
          "picEmail": "johnwick@gmail.com",
          "symtompsName": "LBA",
          "createdAt": "2020-09-03T02:26:32.215Z",
          "updatedAt": "2020-09-11T00:22:47.987Z",
          "ttrAgent": 46.56,
          "ttr": 62.33
        },
        {
          "custAccNum": 1280510,
          "custAccName": "Jatis",
          "ticketId": "INA-1599100080705",
          "userId": 30000041033661,
          "applicationType": 2,
          "senderTypeName": "",
          "categoryId": "E003",
          "category": "Link Connectivity",
          "worklog": [
            {
              "step": 0,
              "status": "checking",
              "dateTime": "2020-09-03T02:28:00.732Z",
              "note": "Tiket sedang di Analisa",
              "createdBy": "Selita Jaya"
            },
            {
              "step": 1,
              "status": "onprogress",
              "dateTime": "2020-09-11T00:07:38.095Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            },
            {
              "step": 2,
              "status": "customerreview",
              "dateTime": null,
              "note": null,
              "createdBy": null
            },
            {
              "step": 3,
              "status": "completed",
              "dateTime": null,
              "note": null,
              "createdBy": null
            },
            {
              "step": 4,
              "status": "onprogress",
              "dateTime": "2020-09-11T00:05:37.748Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            },
            {
              "step": 5,
              "status": "onprogress",
              "dateTime": "2020-09-11T00:07:38.095Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            }
          ],
          "status": "onprogress",
          "description": "Test Description",
          "picName": "Tes Automation",
          "picPhoneNumber": "081233785197",
          "picEmail": "johnwick@gmail.com",
          "symtompsName": "Link Connectivity",
          "createdAt": "2020-09-03T02:28:00.730Z",
          "updatedAt": "2020-09-11T00:07:38.095Z",
          "ttrAgent": 46.53,
          "ttr": 62.3
        },
        {
          "custAccNum": 1280510,
          "custAccName": "Jatis",
          "ticketId": "INA-1599712478261",
          "userId": 30000040703662,
          "applicationType": 2,
          "senderTypeName": "Lorem ipsum",
          "operatorTypeId": 3,
          "categoryId": "E003",
          "category": "Premium",
          "senderTypeId": "",
          "troubleOccurs": {
            "dateTime": "2020-08-31T04:34:24.006Z",
            "logRequest": "request",
            "bNumber": "081233121212",
            "respond": "respond"
          },
          "worklog": [
            {
              "step": 0,
              "status": "checking",
              "dateTime": "2020-09-10T04:34:38.289Z",
              "note": "Request Service Assurance",
              "createdBy": "IMS"
            },
            {
              "step": 1,
              "status": "onprogress",
              "dateTime": "2020-09-10T23:01:57.284Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            },
            {
              "step": 2,
              "status": "customerreview",
              "dateTime": null,
              "note": null,
              "createdBy": null
            },
            {
              "step": 3,
              "status": "completed",
              "dateTime": null,
              "note": null,
              "createdBy": null
            },
            {
              "step": 5,
              "status": "onprogress",
              "dateTime": "2020-09-10T22:57:07.206Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            },
            {
              "step": 5,
              "status": "onprogress",
              "dateTime": "2020-09-10T23:00:06.066Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            },
            {
              "step": 6,
              "status": "onprogress",
              "dateTime": "2020-09-10T23:01:57.284Z",
              "note": "Analyzing issue",
              "createdBy": "occ"
            }
          ],
          "status": "onprogress",
          "description": "-",
          "picName": "Namefull",
          "picPhoneNumber": "08121121",
          "picEmail": "test@gmail.com",
          "symtompsName": "Respon di Delivery Report Undelivered",
          "createdAt": "2020-09-10T04:34:38.288Z",
          "updatedAt": "2020-09-10T23:01:57.284Z",
          "ttrAgent": 4.42,
          "ttr": 20.19
        }
      ]
    },
    "meta": {
      "type": "object",
      "example": {
        "page": 1,
        "size": 10,
        "totalPages": 1,
        "totalData": 9
      }
    },
    "code": {
      "type": "string",
      "example": 200
    },
    "message": {
      "type": "string",
      "example": "success get list ticket internal"
    }
  }
},//response table jadi numpuk karena di schema masuk ke example dan terdapat value objectt array

//remove response table/tambahin isi jika isi data {} array kosong  (???)

//response null if use schema in data response (data:$ref blablabla)