$(window).scroll(function() {
    if($(this).scrollTop() > 50)
    {
        $('.navbar-trans').addClass('afterscroll');
    } else
    {
        $('.navbar-trans').removeClass('afterscroll');
    }

});

$("a[href^='http']").attr("target", "_blank");

function deleteGalleryImage() {
    document.getElementById("demo").style.color = "red";
}


 $(function() {

	var WIDGETS = {};

	WIDGETS.carousel = function carousel(autoslide) {
		var $element,
			position = 0,
			itemCount;

		return {
			init: _init
		}

		function _init(element) {
			var ul = document.createElement("ul"),
				result = "";

			$element = document.querySelector(element);
			itemCount = $element.getElementsByClassName("slide").length;

			for (var count = 0; count < itemCount; count++) {

				if (count === 0) {
					result += '<li class="carousel-target selected" data-target="' + count + '"></li>';
					continue;
				}
				result += '<li class="carousel-target" data-target="' + count + '"></li>';
			}

			ul.innerHTML = result;
			$element.appendChild(ul);

			var width = ul.offsetWidth;
			ul.style.marginLeft = (-width / 2) + "px";

			_bindEvents();
		}

		function _bindEvents() {
			var $next = $element.getElementsByClassName("next")[0];
			var $prev = $element.getElementsByClassName("prev")[0];
			var $selector = $element.getElementsByTagName("ul")[0];
			_addEvent($next, "click", _next);
			_addEvent($prev, "click", _prev);
			_addEvent($selector, "click", _select);
		}

		function _select(evt) {
			var $slides, j = 0,
				target = evt.target || evt.srcElement,
				moveTo = +target.getAttribute("data-target");

			if (!_hasClass(target, "carousel-target") || moveTo === position) return;

			$slides = $element.getElementsByClassName("slide");

			if (moveTo < position) {
				for (j = position; j > moveTo; j--) {
					_removeClass($slides[j], "current");
					_removeClass($slides[j], "prev-slide");
				}
			} else {
				for (j = position; j < moveTo; j++) {
					_removeClass($slides[j], "current");
					_addClass($slides[j], "prev-slide");
				}
			}

			position = moveTo;
			_addClass($slides[j], "current");
			_setSelected(target);
		}

		function _setSelected(item) {
			var items = $element.querySelectorAll("li.carousel-target");

			[].forEach.call(items, function(el) {
				_removeClass(el, "selected");
			});

			_addClass(item, "selected");
		}

		function _next() {
			if (position < itemCount - 1) {
				var current = $element.getElementsByClassName("slide")[position];
				var next = $element.getElementsByClassName("slide")[++position];
				var selected = $element.querySelectorAll("li.carousel-target")[position];

				_removeClass(current, "current");
				_addClass(current, "prev-slide");
				_addClass(next, "current");
				_setSelected(selected);
			}
		}

		function _prev() {
			if (position > 0) {
				var current = $element.getElementsByClassName("slide")[position];
				var prev = $element.getElementsByClassName("slide")[--position];
				var selected = $element.querySelectorAll("li.carousel-target")[position];

				_removeClass(current, "current");
				_removeClass(prev, "prev-slide");
				_addClass(prev, "current");

				_setSelected(selected);
			}
		}

		function _addEvent(el, type, handler) {
			if (el.attachEvent) {
				el.attachEvent('on' + type, handler);
			} else {
				el.addEventListener(type, handler);
			}
		}

		function _removeEvent(el, type, handler) {
			if (el.detachEvent) {
				el.detachEvent('on' + type, handler);
			} else {
				el.removeEventListener(type, handler);
			}
		}

		function _hasClass(el, className) {
			return el.classList ? el.classList.contains(className) : new RegExp('\\b' + className + '\\b').test(el.className);
		}

		function _addClass(el, className) {
			if (el.classList) el.classList.add(className);
			else if (!hasClass(el, className)) el.className += ' ' + className;
		}

		function _removeClass(el, className) {
			if (el.classList) el.classList.remove(className);
			else el.className = el.className.replace(new RegExp('\\b' + className + '\\b', 'g'), '');
		}

	}

	WIDGETS.carousel(true).init("#my-carousel");
	WIDGETS.carousel().init("#my-carousel-2");

});
</script>
<script>
    $(document).ready(function() {

  var carousel = $("#aff");

  carousel.owlCarousel({
    singleItem: true,
    autoPlay: true,
    stopOnHover: true,
    navigation: true,
    pagination: false,
		navigationText: ["<",">"]
  });

});