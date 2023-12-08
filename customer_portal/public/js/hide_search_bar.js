window.onload = function() {
    frappe.call({
        method: "frappe.client.get",
        args: {
            doctype: "User",
            filters: {
                name: frappe.session.user // Retrieves details for the current logged-in user
            },
            fields: ["role_profile_name"] // Fetches the roles associated with the user
        },
        callback: function(r) {
            // console.log(r.message);
            if (r.message && r.message.role_profile_name === "Customer Portal") {
                $('.awesomplete').hide();
                $('.search-icon').hide();
                $('.custom-actions').hide();
                $('.standard-actions').hide();
            }
        }
    });
};



// window.onload = function() {
//     frappe.call({
//         method: 'frappe.client.get_value',
//         args: {
//             doctype: 'User',
//             fieldname: 'role_profile_name',
//             filters: { 'name': 'test_cp_2@gmail.com'}
//         },
//         callback: function(r) {
//             console.log(r);
//             if (r.message && r.message.name === "test_cp_2@gmail.com") {
//                 $('.awesomplete').hide();
//                 $('.search-icon').hide();
//                 $('.custom-actions').hide();
//                 $('.standard-actions').hide();
//             }
//         }
//     });
// };
