fetch("/versions.json")
  .then(response => response.json())
  .then(versions => {
    const container = document.createElement("div");
    container.style.position = "fixed";
    container.style.top = "1rem";
    container.style.right = "1rem";
    container.style.background = "#fff";
    container.style.padding = "0.5rem";
    container.style.border = "1px solid #ccc";
    container.style.zIndex = "1000";

    const label = document.createElement("label");
    label.textContent = "Version: ";
    container.appendChild(label);

    const select = document.createElement("select");
    versions.forEach(v => {
      const option = document.createElement("option");
      option.text = v.version;
      option.value = v.url;
      if (window.location.pathname.startsWith(v.url)) {
        option.selected = true;
      }
      select.appendChild(option);
    });

    select.onchange = () => {
      location.href = select.value;
    };

    container.appendChild(select);
    document.body.appendChild(container);
  });
