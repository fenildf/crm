/**
 * Created by ThinkPad on 13-10-16.
 */
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
        showButtonPanel: true,
        dateFormat: 'yy-mm-dd'
    });
    $("#select_customer_name").change(function () {
        $("#select_contact_name").empty()
        $.ajax({
            type: "POST",
            data: { name: $("#select_customer_name").val() },
            url: "all_contacts",
            dataType: 'json',
            success: function (jsonObject) {
                $.each(jsonObject, function (key, val) {
                    $("#select_contact_name").append("<option>" + val + "</option>");
                });
            }
        });
    });
    $("#edit_sale_opportunity_btn").click(function () {
        $("#edit_sale_opportunity_id").val(current_selected + 1);
    });
});