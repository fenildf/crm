/**
 * Created by ThinkPad on 13-10-16.
 */
// 控制客户页面的table的点击和移动颜色，同时对应“修改客户”按钮的可用性
$(document).ready(function () {
    var current_selected = -1;
    $("#edit_customer_btn").prop("disabled", true);
    $("#table_customer tr:gt(0)").hover(
        function () {
            $(this).addClass("hover_move_customer");
        },
        function () {
            $(this).removeClass("hover_move_customer");
        });
    $("#table_customer tr:gt(0)").click(function () {
        if (current_selected != $(this).parent().find("tr").index($(this))) {
            $("#edit_customer_btn").prop("disabled", false);
            current_selected = $(this).parent().find("tr").index($(this));
        }
        else {
            $("#edit_customer_btn").prop("disabled", true);
            current_selected = -1;
        }
        $(this).toggleClass("hover_click_customer").siblings().removeClass("hover_click_customer");
        $(this).removeClass("hover_move_customer");
        $("#edit_customer_btn").click(function () {
            i = current_selected + 1;
            $("#edit_customer_id").val($('#table_customer tr:nth-child(' + i + ') td:nth-child(1)').text());
            $("#edit_customer_name").val($('#table_customer tr:nth-child(' + i + ') td:nth-child(2)').text());
            $("#edit_customer_kind").val($('#table_customer tr:nth-child(' + i + ') td:nth-child(3)').text());
            $("#edit_customer_phone").val($('#table_customer tr:nth-child(' + i + ') td:nth-child(4)').text());
            $("#edit_customer_address").val($('#table_customer tr:nth-child(' + i + ') td:nth-child(5)').text());
            $("#edit_customer_note").val($('#table_customer tr:nth-child(' + i + ') td:nth-child(8)').text());
        });
    });
});