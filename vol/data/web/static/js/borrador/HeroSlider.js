const slider = {
    hero: document.querySelector('#hero-slider'),
    main: document.querySelector('#slides-main'),
    aux: document.querySelector('#slides-aux'),
    current: document.querySelector('#slider-nav .current'),
    handle: null,
    idle: true,
    activeIndex: -1,
    interval: 3500
};

setHeight(slider.aux, slider.aux.querySelectorAll('.slide-title'));
loadingAnimation();

const loadingAnimation = function () {
    slider.hero.classList.add('ready');
    slider.current.addEventListener('transitionend', start, {
        once: true
    });
}

const start = function () {
	autoplay(true);
	wheelControl();
	window.innerWidth <= 1024 && touchControl();
	slider.aux.addEventListener('transitionend', loaded, {
		once: true
   });
}

const autoplay = function (initial) {
	slider.autoplay = true;
	slider.items = slider.hero.querySelectorAll('[data-index]');
	slider.total = slider.items.length / 2;

	const loop = () => changeSlide('next');

	initial && requestAnimationFrame(loop);
	slider.handle = utils().requestInterval(loop, slider.interval);
}

const changeSlide = function (direction) {
	slider.idle = false;
	slider.hero.classList.remove('prev', 'next');
	if (direction == 'next') {
		slider.activeIndex = (slider.activeIndex + 1) % slider.total;
		slider.hero.classList.add('next');
	} else {
		slider.activeIndex = (slider.activeIndex - 1 + slider.total) % slider.total;
		slider.hero.classList.add('prev');
   }

	//reset classes
	utils().removeClasses(slider.items, ['prev', 'active']);

	//set prev 
	const prevItems = [...slider.items]
		.filter(item => {
			let prevIndex;
			if (slider.hero.classList.contains('prev')) {
				prevIndex = slider.activeIndex == slider.total - 1 ? 0 : slider.activeIndex + 1;
           } else {
               prevIndex = slider.activeIndex == 0 ? slider.total - 1 : slider.activeIndex - 1;
           }

           return item.dataset.index == prevIndex;
       });

   //set active
	const activeItems = [...slider.items]
       .filter(item => {
           return item.dataset.index == slider.activeIndex;
       });

	utils().addClasses(prevItems, ['prev']);
	utils().addClasses(activeItems, ['active']);
	setCurrent();

	const activeImageItem = slider.main.querySelector('.active');
	activeImageItem.addEventListener('transitionend', waitForIdle, {
		once: true
	});
}

const stopAutoplay = function () {
	slider.autoplay = false;
	utils().clearRequestInterval(slider.handle);
}

const touchControl = function () {
	const touchStart = function (e) {
       slider.ts = parseInt(e.changedTouches[0].clientX);
       window.scrollTop = 0;
   }

   const touchMove = function (e) {
       slider.tm = parseInt(e.changedTouches[0].clientX);
       const delta = slider.tm - slider.ts;
       window.scrollTop = 0;

       if (slider.idle) {
           const direction = delta < 0 ? 'next' : 'prev';
           stopAutoplay();
           changeSlide(direction);
       }
   }

	slider.hero.addEventListener('touchstart', touchStart);
	slider.hero.addEventListener('touchmove', touchMove);
}

