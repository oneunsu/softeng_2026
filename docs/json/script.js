/**
 * 통합 인터랙티브 스크립트
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. 현재 페이지 링크 활성화 (Active State)
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    // 2. 스크롤 및 로드 시 등장 애니메이션 (Intersection Observer)
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-up, .project-card, .vision-card, .profile-card').forEach(el => {
        el.classList.add('fade-up');
        observer.observe(el);
    });

    // 3. 메인 Hero 이미지 확대 효과
    if (document.querySelector('.hero-krafton')) {
        const mediaBoxes = document.querySelectorAll('.media-box');
        mediaBoxes.forEach(box => {
            const img = box.querySelector('img');
            if (img) {
                img.style.transform = 'scale(1)';
                requestAnimationFrame(() => {
                    setTimeout(() => {
                        img.style.transform = 'scale(1.05)';
                    }, 150);
                });
            }
        });
    }

    // 4. About interests marquee with hold
    const interestTrack = document.querySelector('.interest-marquee-track');
    const interestItems = interestTrack?.querySelector('.interest-tags');
    if (interestTrack && interestItems) {
        let interestTimeoutId;
        let interestResetTimeoutId;

        const setupInterestMarquee = () => {
            if (!interestTrack.dataset.cloned) {
                interestTrack.dataset.cloned = 'true';
                const clonedItems = interestItems.cloneNode(true);
                clonedItems.setAttribute('aria-hidden', 'true');
                interestTrack.appendChild(clonedItems);
            }

            const trackGap = parseFloat(window.getComputedStyle(interestTrack).columnGap || window.getComputedStyle(interestTrack).gap || '0');
            const originalTags = Array.from(interestItems.children);
            const offsets = [];
            let currentOffset = 0;

            originalTags.forEach((tag, index) => {
                offsets.push(currentOffset);
                currentOffset += tag.getBoundingClientRect().width;
                if (index < originalTags.length - 1) {
                    currentOffset += trackGap;
                }
            });

            const resetOffset = currentOffset + trackGap;
            const holdDuration = 1100;
            const stepDuration = 450;
            let currentIndex = 0;
            const lastIndex = offsets.length - 1;

            clearTimeout(interestTimeoutId);
            clearTimeout(interestResetTimeoutId);
            interestTrack.style.transition = 'none';
            interestTrack.style.transform = 'translateX(0)';
            interestTrack.style.setProperty('--interest-step-duration', `${stepDuration / 1000}s`);

            const queueNextStep = () => {
                interestTimeoutId = window.setTimeout(() => {
                    interestTrack.style.transition = `transform ${stepDuration}ms ease`;

                    if (currentIndex === lastIndex) {
                        interestTrack.style.transform = `translateX(${-resetOffset}px)`;
                        interestResetTimeoutId = window.setTimeout(() => {
                            interestTrack.style.transition = 'none';
                            interestTrack.style.transform = 'translateX(0)';
                            currentIndex = 0;
                            requestAnimationFrame(() => {
                                requestAnimationFrame(queueNextStep);
                            });
                        }, stepDuration);
                        return;
                    }

                    currentIndex += 1;
                    interestTrack.style.transform = `translateX(${-offsets[currentIndex]}px)`;
                    interestResetTimeoutId = window.setTimeout(() => {
                        queueNextStep();
                    }, stepDuration);
                }, holdDuration);
            };

            requestAnimationFrame(() => {
                requestAnimationFrame(queueNextStep);
            });
        };

        window.addEventListener('load', setupInterestMarquee, { once: true });
        window.addEventListener('resize', setupInterestMarquee);
        setupInterestMarquee();
    }

    // 5. Projects slider
    const projectTrack = document.querySelector('.project-grid');
    const projectSlides = projectTrack ? Array.from(projectTrack.querySelectorAll('.project-card')) : [];
    const projectPrevBtn = document.querySelector('.project-nav-prev');
    const projectNextBtn = document.querySelector('.project-nav-next');
    const projectCurrent = document.querySelector('.project-slider-current');
    const projectTotal = document.querySelector('.project-slider-total');

    if (projectTrack && projectSlides.length && projectPrevBtn && projectNextBtn) {
        let currentSlide = 0;

        const updateProjectSlider = () => {
            projectTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
            projectPrevBtn.disabled = currentSlide === 0;
            projectNextBtn.disabled = currentSlide === projectSlides.length - 1;

            if (projectCurrent) {
                projectCurrent.textContent = String(currentSlide + 1);
            }

            if (projectTotal) {
                projectTotal.textContent = String(projectSlides.length);
            }
        };

        projectPrevBtn.addEventListener('click', () => {
            if (currentSlide > 0) {
                currentSlide -= 1;
                updateProjectSlider();
            }
        });

        projectNextBtn.addEventListener('click', () => {
            if (currentSlide < projectSlides.length - 1) {
                currentSlide += 1;
                updateProjectSlider();
            }
        });

        updateProjectSlider();
    }

    // 6. 소셜 버튼 클릭 이벤트 (간단 알림)
    const socialBtns = document.querySelectorAll('.social-btn');
    socialBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (btn.getAttribute('href') === '#') {
                e.preventDefault();
                console.log(`${btn.textContent.trim()} link is not set yet.`);
            }
        });
    });
});
