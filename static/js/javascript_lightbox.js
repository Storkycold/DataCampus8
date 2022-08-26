var $searchInputClick = _$('.search_input').find('a');

$searchInputClick.on('click', searchText );

var _$searchInput = _$('.search_input').find('input');

_$searchInput.keyup(function(e) {
if(e.keyCode == 13) {   
    searchText( );
}

});

function searchText($e){
var thisText = $('aside .menu_box .search .search_input input').val();

if( thisText == '' ){
    $('aside .menu_box .search .search_input input').val('').blur(); //blur 처리하여 모바일에서 인풋 포커스 없애서 키패드 감추기
    alert('검색어가 없습니다.');
} 

else {
    window.location.href = ("/" + "/search/search_list.asp?q=" + encodeURIComponent(thisText));                                                                //이동시킬 페이지                     //encodeURIComponent로 변환하여 넘기기 
}
}
