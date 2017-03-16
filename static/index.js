function start_service() {
  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'start', false);
  xhr.send();

  if (xhr.status != 200) {
    alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
  } else {
    location.reload(true);
  }
}

function restart_service() {
  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'restart', false);
  xhr.send();

  if (xhr.status != 200) {
    alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
  } else {
    location.reload(true);
  }
}

function stop_service() {
  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'stop', false);
  xhr.send();

  if (xhr.status != 200) {
    alert('Ошибка ' + xhr.status + ': ' + xhr.statusText);
  } else {
    location.reload(true);
  }
}
