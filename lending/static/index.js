
var app = new Vue({
    el: '#app',
    data() {
        return {
            owner_name: "",
            owner_email: "",
            tax_id: "",
            business_name: "",
            requested_amount: "",
            security_number: ""
        };
    },
    methods: {
        agregarArticulo: function() {
            var formData = new FormData();

            formData.append('owner_name', this.owner_name);
            formData.append('owner_email', this.owner_email);
            formData.append('tax_id', this.tax_id);
            formData.append('business_name', this.business_name);
            formData.append('requested_amount', this.requested_amount);
            formData.append('security_number', this.security_number);

            axios.post(
                'http://0.0.0.0:8888/response/',
                formData
            ).then(response => {
                this.results = response.data;
                var icon = 'question';
                var title = 'Reviewing';
                if (this.results.Response === 'Approved') {
                    icon = 'success';
                    title = 'Approved';
                } else if (this.results.Response === 'Declined') {
                    icon = 'error';
                    title = 'Declined';
                }

                var object = '';
                for (var prop in this.results) {
                   object += `<p><b>${prop}:</b> ${this.results[prop]}</p>`;
                }

                Swal.fire({
                    icon: icon,
                    title: title,
                    html: object
                });
            }).catch(function (error) {
                console.log(error);
                console.log('***************************');
            });
        }
    }
});
