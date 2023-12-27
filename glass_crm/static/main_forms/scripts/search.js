document.getElementById('search-input').addEventListener('input', function() {
    var searchText = this.value;
    var rows = document.querySelectorAll('.table-container tbody tr');
  
    // Если поле ввода пустое, удаляем все подсветки
    if (searchText === '') {
      rows.forEach(function(row) {
        var cells = row.getElementsByTagName('td');
        for (var i = 0; i < cells.length; i++) {
          var cell = cells[i];
          cell.innerHTML = cell.textContent;
        }
      });
      return;
    }
  
    // Создаем регулярное выражение с учетом регистра для поиска текста внутри ячеек
    var searchRegex = new RegExp(searchText, 'i');
  
    rows.forEach(function(row) {
      var cells = row.getElementsByTagName('td');
      var matchFound = false;
  
      for (var i = 0; i < cells.length; i++) {
        var cell = cells[i];
        var cellText = cell.textContent;
  
        // Если найдено совпадение по регулярному выражению,
        // заменяем совпадающую часть текста на подсвеченную версию
        if (searchRegex.test(cellText)) {
          var highlightedText = cellText.replace(searchRegex, function(match) {
            return '<span class="highlight">' + match + '</span>';
          });
          cell.innerHTML = highlightedText;
          matchFound = true;
        } else {
          cell.innerHTML = cellText;
        }
      }
  
      // Показываем или скрываем строку в зависимости от наличия совпадений в ячейках
      if (matchFound) {
        row.style.display = '';
      } else {
        row.style.display = 'none';
      }
    });
  });
  