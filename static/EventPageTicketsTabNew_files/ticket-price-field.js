var hook_ticket_price_field = function() {
  $("[data-toggle=ticket-revenue-field]").each(function(n) {
    var $input = $(this);
    var $seller_income_field = $input.prev('.ticket-seller-revenue');

    $input.on('keyup change', function() {{
        var x_buyer = $(this).val();

        if (x_buyer > 0.0) {
          var x_seller = x_seller_f(x_buyer)
          x_seller = parseFloat(x_seller).toFixed(2);

          // TODO: eventually we should show a different text depending on how the fee is being paid
          //var fee_explaination = "This amount factors in the cost of processing the buyer's debit or credit card info (we use Stripe to do this), and Agora's booking fee. We donate 100% of this booking fee to charity.";
          var fee_explaination = "The small processing cost (which includes Stripe’s processing fee) will be covered by the buyer.";
          var field_str = 'You will receive <abbr data-toggle="tooltip" data-placement="top" data-original-title="' + fee_explaination + '">'
                            + "£" + x_seller + "</abbr>";

          $seller_income_field.html(field_str);
          $('[data-toggle=tooltip]').tooltip();
        }
        else{
          $seller_income_field.html("");
        }
    }})
  })
}
