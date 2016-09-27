function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function update_cities(state){
    var city_select_box = $('#id_city');
    $.ajax({
        url: '/states_cities/',
        data: {state: state},
        beforeSend: function(){
            city_select_box.empty();
            $('#city_loading').show();
        },
        success: function(data){
            update_select_box(city_select_box, data);
            select_filtered_city();
        },
        complete: function(){
            $('#city_loading').hide();
        }
    });
};
function update_select_box(obj, data){
    $.each(data, function(key, value){
        obj.append($('<option></option>')
            .attr('value', value).text(value));
    });
};

$('#id_state').on('change', function(e){
    obj = $(this)
    update_cities(obj.val());
});

$('.clear_filters').on('click', function(e){
    $(this).closest('form').find('input[type=text], textarea').val('');
    $('#id_bedrooms').val('');
    $('#id_bathrooms_full').val('');
});



$(".reset").click(function() {
    $(this).closest('form').find("input[type=text], textarea").val("");
});



function init_cities(){
    obj = $('#id_state');
    update_cities(obj.val());
};

function select_filtered_city(){
    var city = getParameterByName('city');
    $('#id_city').find('[value="' + city + '"]').attr("selected",true);
}

$(document).ready(function(){
    init_cities();
});