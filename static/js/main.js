/**
 * Handling old_ticket_id disabled enabled case
 */
const old_ticket_id = document.getElementById('id_old_ticket_id');
const already_raised = document.getElementById('id_already_raised');

if (already_raised) {
  if (already_raised.checked) {
    old_ticket_id.disabled = false;
  } else {
    old_ticket_id.disabled = true;
  }

  already_raised.onchange = function () {
    if (already_raised.checked) {
      old_ticket_id.disabled = false;
    } else {
      old_ticket_id.disabled = true;
      if (old_ticket_id.value != null) {
        old_ticket_id.value = null;
      }
    }
  };
}

/* ------------------------------------------------------------------------------------------------ */
