const rules = {
  required(value) {
    return !!value || "Esse campo é obrigatório";
  },
};

export default rules;
