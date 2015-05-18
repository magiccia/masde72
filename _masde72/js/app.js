var $window;
var $videos;
var $intro;

// Resize intro box
var fitIntro = function(e) {
  var height = $window.height();
  $intro.height(height);
}

$(function() {
  // Populate variables
  $window = $(window);
  $videos = $('.video');
  $intro = $('.intro');

  // Behaviors
  $videos.fitVids();
  fitIntro();
  $window.on('resize', fitIntro);
  $.localScroll({
    'duration': 500
  });
  $("img").unveil(200);
});
