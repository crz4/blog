
fetch('/api/appointments/available/', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
})
.then(data => {
  console.log('Доступные даты и специалисты:', data);
})
.catch(error => {
  console.error('Ошибка при получении данных:', error);
});