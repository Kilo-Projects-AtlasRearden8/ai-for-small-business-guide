document.addEventListener('DOMContentLoaded', function () {
  var printBtn = document.querySelector('.print-btn');
  if (printBtn) {
    printBtn.style.display = 'inline-block';
  }

  var links = document.querySelectorAll('.site-nav a');
  links.forEach(function (link) {
    link.addEventListener('focus', function () {
      this.style.outline = '2px solid #a65a3c';
    });
    link.addEventListener('blur', function () {
      this.style.outline = '';
    });
  });
});
