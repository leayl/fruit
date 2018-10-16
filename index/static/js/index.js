  $(function () {
    loadGoods()
  })
  function loadGoods() {
      $.get('/goods/', function (data) {
          $.each(data, function (i, obj) {
              type = JSON.parse(obj.type);
              goods = JSON.parse(obj.goods);
              $div1 = $("<div class='item'></div>")
              $p1 = $("<p class='title'></p>")
              $a1 = $("<a href='#'>更多</a>")
              $img1 = $("<img src='/" + type.picture + "'>")
              $p1.append($a1)
              $p1.append($img1)
              $ul = $("<ul></ul>")
              $.each(goods, function (j, good) {
                  var clas
                  if(j == 4){
                      clas="'no-margin'"
                  }else{
                      clas=""
                  }
                  $li = $("<li class="+clas+"></li>")
                  $p2 = $("<p></p>")
                  $img2 = $("<img src='/" + good.fields.picture + "'>")
                  $p2.append($img2)
                  $div2 = $("<div class='content'></div>")
                  $a2 = $("<a href='#' class='cart'></a>")
                  $img3 = $("<img src='/static/images/cart.png'>")
                  $a2.append($img3)
                  $p3 = $("<p>" + good.fields.title + "</p>")
                  $span = $("<span>￥" + good.fields.price + "/1" + good.fields.spec + "</span>")
                  $div2.append($a2)
                  $div2.append($p3)
                  $div2.append($span)
                  $li.append($p2)
                  $li.append($div2)
                  $ul.append($li)
              })
              $div1.append($p1)
              $div1.append($ul)
              $("#main").append($div1)
          })
      },'json')
  }