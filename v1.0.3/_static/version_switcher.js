fetch("/versions.json")
  .then((response) => response.json())
  .then((versions) => {
    const current = location.pathname.split("/")[1];

    const container = document.getElementById("version-switcher-container");
    if (!container) return;

    const label = document.createElement("label");
    label.textContent = "Version: ";
    label.style.marginRight = "5px";

    const select = document.createElement("select");
    select.id = "version-switcher";

    versions.forEach((v) => {
      const option = document.createElement("option");
      option.value = v.url || v.name;
      option.textContent = v.name;
      if (v.name === current || v.url === current) {
        option.selected = true;
      }
      select.appendChild(option);
    });

    select.onchange = () => {
      const selected = select.value;
      const rest = location.pathname.split("/").slice(2).join("/");
      location.href = `/${selected}/${rest}`;
    };

    container.appendChild(label);
    container.appendChild(select);
  });
