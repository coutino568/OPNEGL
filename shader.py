

vertex_shader = '''
#version 450 core

layout (location =0) in vec3 position;
layout (location =1 ) in vec2 texcoords;
layout (location = 2) in vec3 normals;
uniform float time;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;


out vec2 UVs;
out vec3 outNormals;


void main ()
{
    UVs=texcoords;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position,1.0);  
    outNormals = (modelMatrix * vec4(normals,0.0)).xyz;  
}
'''

fragment_shader = '''
#version 450 core




in vec2 UVs;
in vec3 outNormals;

uniform vec3 light;
uniform sampler2D tex;


out vec4 fragcolor;


void main()
{
    float intensity = dot(outNormals, -light);
    float intensity2= min(1, intensity);
    float intensity3= max(0.2,intensity2);
    fragcolor = texture( tex, UVs)* intensity3;
    
}


'''