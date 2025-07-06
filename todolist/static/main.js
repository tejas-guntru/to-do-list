document.addEventListener('DOMContentLoaded', function() {
  // Add active class to current page link
  const currentPage = location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('nav a');
  
  navLinks.forEach(link => {
    const linkPage = link.getAttribute('href').split('/').pop();
    if (currentPage.includes(linkPage)) {
      link.classList.add('active');
    }
  });
  
  // Animate form elements
  const formGroups = document.querySelectorAll('.form-group');
  formGroups.forEach((group, index) => {
    group.classList.add('animate', `delay-${index % 3 + 1}`);
  });
  
  // Confirmation for delete actions
  const deleteButtons = document.querySelectorAll('.btn.delete');
  deleteButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      if (!confirm('Are you sure you want to delete this task?')) {
        e.preventDefault();
      }
    });
  });
  
  // Date picker enhancement
  const dateInputs = document.querySelectorAll('input[type="date"]');
  dateInputs.forEach(input => {
    if (!input.value) {
      const today = new Date().toISOString().split('T')[0];
      input.min = today;
    }
  });
});