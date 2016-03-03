$(document).ready(function () {
    $(".caption").next().hide();
    $(".caption").click(function () {

        $header = $(this);
        $content = $header.next();

        $others = $header.parent().siblings();

        $others.find(".content").hide();

        $content.slideToggle(500,function(){
            if ($content.is(":visible")) {
                $header.removeClass("hover");
            }
        });

    });

    $(".caption").hover(
        function(){
            $content = $(this).next();

            if($content.is(":hidden")) {
                $(this).addClass("hover");
            }
        },
        function(){
            $(this).removeClass("hover");
        }
    );
});