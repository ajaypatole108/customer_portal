import frappe
import requests
import json

@frappe.whitelist()
def create_item(doc, event):
    # url = "https://n8n.dhupargroup.com/webhook-test/00b9f0ed-0e62-48d6-98ef-07724d8ad05a" # Test

    url = "https://n8n.dhupargroup.com/webhook/00b9f0ed-0e62-48d6-98ef-07724d8ad05a" # Production
  
    item_tax_template = [itt.item_tax_template for itt in doc.taxes]
    tax_category = [tc.tax_category for tc in doc.taxes]
    valid_from = [vf.valid_from for vf in doc.taxes]

    print(item_tax_template)
    print(tax_category)
    print(valid_from)
    data = {
                "item_code": f"{ doc.item_code }",
                "item_name": f"{ doc.item_name }",
                "item_group": f"{ doc.item_group }",
                "brand": f"{ doc.brand }",
                "gst_hsn_code": f"{ doc.gst_hsn_code }",
                "default_uom": f"{ doc.stock_uom }",
                "description": f"{ doc.description }",
                "taxes": [
                           {"item_tax_template": f"{item_tax_template}"},
                           {"tax_category": f"{tax_category}"},
                           {"valid_from":f"{valid_from}"}
                         ]
           }

    headers = {
      'content-type': "application/json",
      'cache-control': "no-cache"
		}

    response = requests.post(url, data=json.dumps(data), headers=headers)