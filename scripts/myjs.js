$(document).ready(function () {
    $(".caption").next().hide();
    $(".caption").click(function () {

        $header = $(this);
        //getting the next element
        $content = $header.next();
        //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
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