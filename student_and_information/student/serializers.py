from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['s_name','s_tel']

    def to_representation(self, instance): # 将实例序列化
        data = super().to_representation(instance)
        try:
            data['s_addr'] = instance.studentinfo.s_addr
        except Exception as e:
            data['s_addr'] = ""
        return data