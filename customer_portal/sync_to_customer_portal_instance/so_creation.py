import frappe
import requests
import json

frappe.whitelist()
def sales_order_creation(doc,event):
    # url = 'https://n8n.dhupargroup.com/webhook-test/14865644-3df7-4b45-9a86-9530cbf9e5ef' # Test 

    url = 'https://n8n.dhupargroup.com/webhook/14865644-3df7-4b45-9a86-9530cbf9e5ef' # Production

    data = {
                "doc": f"{doc.name}"
           }

    headers = {
                'content-type': "application/json",
                'cache-control': "no-cache"
            }

    response = requests.post(url, data=json.dumps(data), headers=headers)
