// 控制客户页面的table的点击和移动颜色，同时对应“修改客户”按钮的可用性
$(document).ready(function () {
    var current_selected = -1;
    $("#edit_sale_opportunity_btn").prop("disabled", true);
    $("#table_sale_opportunity tr:gt(0)").hover(
        function () {
            $(this).addClass("hover_move_sale_opportunity");
        },
        function () {
            $(this).removeClass("hover_move_sale_opportunity");
        });

    $("#table_sale_opportunity tr:gt(0)").click(function () {
        if (current_selected != $(this).parent().find("tr").index($(this))) {
            $("#edit_sale_opportunity_btn").prop("disabled", false);
            current_selected = $(this).parent().find("tr").index($(this));
        }
        else {
            $("#edit_sale_opportunity_btn").prop("disabled", true);
            current_selected = -1;
        }
        $(this).toggleClass("hover_click_sale_opportunity").siblings().removeClass("hover_click_sale_opportunity");
        $(this).removeClass("hover_move_sale_opportunity");
    });
    $(".datepicker").datepicker({
        numberOfMonths: 2,  //显示两个月
        showWeek: true,
        showButtonPanel: true
//        minDate: 0  //从当前日期起可选
    });
    $("#new_sale_opportunity_btn").click(function () {
        if ($('#new_customer_name option').size() == 1) {
            $.ajax({
                type: "POST",
                url: "all_customers",
                dataType: 'json',
                success: function (jsonObject) {
                    $.each(jsonObject, function (key, val) {
                        $("#new_customer_name").append("<option>" + val + "</option>");
                    });
                }
            });
        }
    });
});