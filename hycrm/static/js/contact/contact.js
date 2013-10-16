/**
 * Created by ThinkPad on 13-10-16.
 */
// 控制客户页面的table的点击和移动颜色，同时对应“修改客户”按钮的可用性
$(document).ready(function () {
    var current_selected = -1;
    $("#edit_contact_btn").prop("disabled", true);
    $("#table_contact tr:gt(0)").hover(
        function () {
            $(this).addClass("hover_move_contact");
        },
        function () {
            $(this).removeClass("hover_move_contact");
        });

    $("#table_contact tr:gt(0)").click(function () {
        if (current_selected != $(this).parent().find("tr").index($(this))) {
            $("#edit_contact_btn").prop("disabled", false);
            current_selected = $(this).parent().find("tr").index($(this));
        }
        else {
            $("#edit_contact_btn").prop("disabled", true);
            current_selected = -1;
        }
        $(this).toggleClass("hover_click_contact").siblings().removeClass("hover_click_contact");
        $(this).removeClass("hover_move_contact");
    });
    $("#new_contact_btn").click(function () {
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
            $("#edit_contact_btn").click(function () {
            if ($('#edit_customer_name option').size() == 1) {
                $.ajax({
                    type: "POST",
                    url: "all_customers",
                    dataType: 'json',
                    success: function (jsonObject) {
                        $.each(jsonObject, function (key, val) {
                            $("#edit_customer_name").append("<option>" + val + "</option>");
                        });
                    }
                });
            }
            i = current_selected + 1;
            $("#edit_contact_id").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(1)').text());
            $("#edit_contact_name").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(2)').text());
            $("#edit_contact_duty").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(3)').text());
            $("#edit_contact_gender").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(4)').text());
            $("#edit_customer_name").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(5)').text());
            $("#edit_contact_department").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(7)').text());
            $("#edit_contact_telephone").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(8)').text());
            $("#edit_contact_mobile").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(9)').text());
            $("#edit_contact_email").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(10)').text());
            $("#edit_contact_note").val($('#table_contact tr:nth-child(' + i + ') td:nth-child(13)').text());
        });
    //点击"对应客户"选择框，从数据库得到对应的客户数据用ajax？

});