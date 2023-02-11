# Copyright (c) 2023, Janhvi Patil and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Message(Document):
    pass


@frappe.whitelist(methods=['POST'])
def send_message(channel_id, user_id, text):
    doc = frappe.get_doc({
        'doctype': 'Message',
        'channel_id': channel_id,
        'text': text,
        'user_id': user_id
    })
    doc.insert()
    frappe.db.commit()
    return "message sent"
