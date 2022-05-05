$(".whatsapp__box").click(function(){
    $(".whatsapp_chat_box").css("display","block")
    $(".whatsapp__box").css("display","none")
    $(".message__time").html(`${new Date().getHours()} : ${new Date().getMinutes()}`)
  })
  $(".chat_box_close").click(function(){
    $(".whatsapp_chat_box").css("display","none")
    $(".whatsapp__box").css("display","grid")
  })
$(".navbar-toggler").click(function(){
    if(!$(".navbar-collapse").hasClass("show")){
      $(".whatsapp__box").css("display","none")
    }
    else{
      $(".whatsapp__box").css("display","grid")
    }
  })